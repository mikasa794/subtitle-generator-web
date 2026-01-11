'use client';

import { useState, useEffect, useRef } from 'react';
import Link from 'next/link';
import { ChevronLeft, BookOpen, Quote, Sparkles, Repeat, SkipBack, SkipForward, Play, Pause, Heart } from 'lucide-react';
import { LingoClip } from '@/lib/feishu';

// Helper to get ID
import YouTube from 'react-youtube';

function getYouTubeId(url: string) {
    const regExp = /^.*(youtu.be\/|v\/|u\/\w\/|embed\/|watch\?v=|&v=)([^#&?]*).*/;
    const match = url?.match(regExp);
    return (match && match[2].length === 11) ? match[2] : null;
}

export default function LingoPlayerClient({ clip }: { clip: LingoClip }) {
    const videoId = getYouTubeId(clip.videoUrl);
    const [transcriptData, setTranscriptData] = useState<any[]>([]);
    const [activeContext, setActiveContext] = useState<any>(null); // The data for the sidebar
    const [player, setPlayer] = useState<any>(null); // State to hold YT player reference if using library, but for iframe we use ID
    const [currentTime, setCurrentTime] = useState(0);

    // Current active subtitle for Overlay
    const [activeSubtitle, setActiveSubtitle] = useState<any>(null);

    const [syncOffset, setSyncOffset] = useState(0); // User manual sync offset
    const [isLooping, setIsLooping] = useState(false); // SHADOWING: Loop mode

    const scrollContainerRef = useRef<HTMLDivElement>(null);
    const activeItemRef = useRef<HTMLDivElement>(null);

    const [isHoveringList, setIsHoveringList] = useState(false);

    // Auto-Scroll to active item (Only if not hovering)
    useEffect(() => {
        if (!isHoveringList && activeItemRef.current && scrollContainerRef.current) {
            activeItemRef.current.scrollIntoView({ behavior: 'smooth', block: 'center' });
        }
    }, [currentTime, isHoveringList]); // Trigger on time update

    useEffect(() => {
        if (clip.transcript) {
            try {
                const parsed = JSON.parse(clip.transcript);
                if (Array.isArray(parsed)) {
                    setTranscriptData(parsed);
                }
            } catch (e) {
                // fallback or leave empty
            }
        }
    }, [clip.transcript]);

    // Timer to update current time from player
    useEffect(() => {
        let interval: NodeJS.Timeout;
        if (player) {
            interval = setInterval(() => {
                const t = player.getCurrentTime();
                setCurrentTime(t);

                // Determine active subtitle for overlay
                // Find the item where t is between start and end (with offset)
                const currentIdx = transcriptData.findIndex(item => {
                    const adjustedStart = item.start + syncOffset;
                    const adjustedEnd = item.end + syncOffset;
                    return t >= adjustedStart && t <= adjustedEnd;
                });

                if (currentIdx !== -1) {
                    const current = transcriptData[currentIdx];
                    setActiveSubtitle(current);

                    // NEW: Auto-Sync Sidebar Context (if not manually exploring)
                    if (!isHoveringList) {
                        // console.log("🔄 Syncing Context:", current.text_source, current.context?.vocab?.length);
                        setActiveContext({
                            ...current.context,
                            source: current.text_source,
                            target: current.text_target
                        });
                    } else {
                        // console.log("⚠️ Sync Blocked by Hover");
                    }

                    // SHADOWING: Loop Logic
                    if (isLooping) {
                        const adjustedEnd = current.end + syncOffset;
                        // Seek back if near end (leave 0.1s buffer or exact?)
                        // Using 0.2s before end to avoid gap? No, standard loop seeks at end.
                        if (t >= adjustedEnd - 0.1) {
                            player.seekTo(current.start + syncOffset, true);
                        }
                    }

                } else {
                    setActiveSubtitle(null);
                    // Optional: Clear context or keep last? 
                    // Let's keep last context so it doesn't flash empty during tiny gaps, 
                    // unless it's a long gap. For now, keeping last is safer for UX.
                }

            }, 100); // 100ms for smoother sync
        }
        return () => clearInterval(interval);
    }, [player, transcriptData, syncOffset, isHoveringList, isLooping]);

    // Keyboard Shortcuts
    useEffect(() => {
        const handleKeyDown = (e: KeyboardEvent) => {
            if (!player) return;
            // Ignore if typing in inputs
            if (e.target instanceof HTMLInputElement || e.target instanceof HTMLTextAreaElement) return;

            // Helper to find current index based on time (more robust than activeSubtitle state which might lag)
            const getCurrentIndex = () => {
                const t = player.getCurrentTime();
                // Find closest match or exactly current
                // If in gap, find Next one? Or Previous one?
                // Usually we want the one *active* or the one *just after*.
                // Let's iterate.
                for (let i = 0; i < transcriptData.length; i++) {
                    const item = transcriptData[i];
                    if (t < item.end + syncOffset) return i;
                }
                return transcriptData.length - 1;
            };

            switch (e.key) {
                case 'ArrowLeft':
                    e.preventDefault();
                    if (e.shiftKey) {
                        player.seekTo(Math.max(0, currentTime - 5), true);
                    } else {
                        // Prev Sentence
                        const idx = getCurrentIndex();
                        if (idx > 0) {
                            // If we are significantly into the current sentence, jump to ITS start?
                            // Or jump to PREVIOUS?
                            // Standard: Click Once -> Start of Current. Click Twice -> Start of Prev.
                            const currentItem = transcriptData[idx];
                            const t = player.getCurrentTime();
                            const start = currentItem.start + syncOffset;

                            if (t > start + 1.0) { // If played more than 1s, restart current
                                player.seekTo(start, true);
                            } else {
                                // Jump to prev
                                const prevItem = transcriptData[idx - 1];
                                player.seekTo(prevItem.start + syncOffset, true);
                            }
                        } else {
                            player.seekTo(0, true);
                        }
                    }
                    break;
                case 'ArrowRight':
                    e.preventDefault();
                    if (e.shiftKey) {
                        player.seekTo(currentTime + 5, true);
                    } else {
                        // Next Sentence
                        const idx = getCurrentIndex();
                        if (idx < transcriptData.length - 1) {
                            // If currently in a sentence, jump to Next.
                            // If in gap, jump to Next.
                            // getCurrentIndex returns the one we are IN or BEFORE.
                            // So simply idx + 1?

                            // Refine getCurrentIndex logic above: it returns first item where end > t.
                            // So it IS the current or next upcoming.
                            // So seek to that item's END? No, seek to Next Item's Start.
                            // But if we are IN item 5. getCurrentIndex returns 5.
                            // We want to go to 6.

                            const nextItem = transcriptData[idx + 1];
                            player.seekTo(nextItem.start + syncOffset, true);
                        }
                    }
                    break;
                case ' ':
                    e.preventDefault();
                    if (player.getPlayerState() === 1) player.pauseVideo();
                    else player.playVideo();
                    break;
                case 'r':
                case 'R':
                    setIsLooping(prev => !prev);
                    break;
                case 'Enter':
                    handleEnterSave();
                    break;
            }
        };

        window.addEventListener('keydown', handleKeyDown);
        return () => window.removeEventListener('keydown', handleKeyDown);
    }, [player, currentTime, transcriptData, syncOffset]);


    // Adjust Sync
    const adjustSync = (delta: number) => {
        setSyncOffset(prev => Math.round((prev + delta) * 10) / 10);
    };

    // --- VOCAB SAVING LOGIC ---
    const [savingVocab, setSavingVocab] = useState<string | null>(null); // Word being saved
    const [savedVocabs, setSavedVocabs] = useState<Set<string>>(new Set());

    const handleSaveVocab = async (word: string, meaning: string) => {
        if (savingVocab || savedVocabs.has(word)) return;
        setSavingVocab(word);

        try {
            // Find context
            const ctxSentence = activeContext?.source || activeSubtitle?.text_source || "";
            const t = player ? player.getCurrentTime() : 0;

            const res = await fetch('/api/vocab/v2', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    word,
                    meaning,
                    context: ctxSentence,
                    videoTitle: clip.title,
                    videoUrl: clip.videoUrl,
                    timestamp: t
                })
            });

            if (res.ok) {
                setSavedVocabs(prev => new Set(prev).add(word));
                // Show toast? Or just heart status change
            } else {
                const err = await res.json();
                alert("Save Failed: " + (err.error || "Unknown Error"));
            }
        } catch (e) {
            console.error("Failed to save vocab");
            alert("Network Error: Failed to save");
        } finally {
            setSavingVocab(null);
        }
    };

    const handleEnterSave = () => {
        if (activeContext && activeContext.vocab && activeContext.vocab.length > 0) {
            // Save the first one for now as MVP shortcut
            const v = activeContext.vocab[0];
            handleSaveVocab(v.word, v.meaning);
        }
    };

    // Handle Hover
    const handleLineHover = (item: any) => {
        if (item.context) {
            setActiveContext({
                ...item.context,
                source: item.text_source,
                target: item.text_target
            });
        }
    };

    // --- Audio Features ---

    // 1. Text-to-Speech for Words
    const speakWord = (word: string) => {
        const utterance = new SpeechSynthesisUtterance(word);
        utterance.lang = 'en-US';
        utterance.rate = 0.9;
        window.speechSynthesis.speak(utterance);
    };

    const onReady = (event: any) => {
        setPlayer(event.target);
        // Attempt to turn off captions again
        event.target.unloadModule('captions');
        event.target.loadModule('cc');
    };

    const seekTo = (seconds: number) => {
        if (player) {
            player.seekTo(seconds, true);
            player.playVideo();
        }
    };

    return (
        <div className="h-screen bg-black text-white flex flex-col font-sans selection:bg-teal-500/30">
            {/* Header */}
            <header className="h-[60px] flex items-center px-6 border-b border-white/10 bg-[#1c1c1e] shrink-0 z-20">
                <Link href="/lingo" className="flex items-center gap-2 text-gray-300 hover:text-white transition-colors">
                    <ChevronLeft className="w-5 h-5" />
                    <span className="font-medium">Back</span>
                </Link>
                <div className="ml-6 border-l border-white/10 pl-6">
                    <h1 className="text-lg font-semibold truncate max-w-xl text-gray-200">{clip.title}</h1>
                </div>


            </header>

            <div className="flex-1 flex flex-col md:flex-row overflow-hidden">
                {/* ID: Main Content (Video + Subtitle Split) */}
                <div className="flex-1 relative bg-black flex flex-col min-w-0 h-[50vh] md:h-auto">

                    {/* Video Layer */}
                    <div className="relative flex-none aspect-video md:h-[60%] w-full bg-black">
                        {videoId ? (
                            <>
                                <YouTube
                                    videoId={videoId}
                                    className="w-full h-full"
                                    iframeClassName="w-full h-full"
                                    onReady={onReady}
                                    opts={{
                                        playerVars: {
                                            autoplay: 0,
                                            controls: 1,
                                            cc_load_policy: 0, // Force captions OFF
                                            iv_load_policy: 3, // Turn off annotations
                                            fs: 0, // Disable fullscreen button to keep overlay visible (optional)
                                            rel: 0
                                        }
                                    }}
                                />

                                {/* --- OVERLAY SUBTITLES (The "Video Inner Subtitle") --- */}
                                {/* Positioned at the bottom of the video player area */}
                                {activeSubtitle && (
                                    <div className="absolute bottom-[10%] left-0 right-0 flex flex-col items-center justify-center pointer-events-none z-10 px-4 text-center">
                                        <div className="bg-black/60 backdrop-blur-sm px-6 py-3 rounded-xl shadow-lg transition-all duration-200 pointer-events-auto">
                                            {/* Source: One Long Line (as requested), Larger Font */}
                                            <p className="text-xl md:text-2xl font-bold text-white mb-1 drop-shadow-md leading-relaxed tracking-wide">
                                                {activeSubtitle.text_source_ruby ? (
                                                    <span dangerouslySetInnerHTML={{ __html: activeSubtitle.text_source_ruby }} />
                                                ) : (
                                                    activeSubtitle.text_source
                                                )}
                                            </p>

                                            {/* Target: Chinese Below, Smaller, Distinct Color */}
                                            <p className="text-base md:text-lg text-teal-300 font-medium opacity-90 drop-shadow-sm">
                                                {activeSubtitle.text_target}
                                            </p>
                                        </div>
                                    </div>
                                )}
                            </>
                        ) : (
                            <div className="flex items-center justify-center h-full text-gray-500">Video Invalid</div>
                        )}
                    </div>

                    {/* SHADOWING TOOLBAR */}
                    <div className="h-14 bg-[#18181b] border-y border-white/5 flex items-center justify-between px-6 shrink-0 z-20">
                        <div className="flex items-center gap-4">
                            <span className="text-xs font-bold text-teal-500 tracking-wider uppercase">Interpreter Mode</span>
                        </div>

                        <div className="flex items-center gap-2 md:gap-4">
                            {/* Prev Sentence */}
                            <button
                                onClick={() => {
                                    // Trigger Left Arrow logic manually
                                    window.dispatchEvent(new KeyboardEvent('keydown', { key: 'ArrowLeft' }));
                                }}
                                className="p-2 rounded-full hover:bg-white/10 text-gray-400 hover:text-white transition-colors"
                                title="Prev Sentence (Left Arrow)"
                            >
                                <SkipBack className="w-5 h-5" />
                            </button>

                            {/* Play/Pause */}
                            <button
                                onClick={() => {
                                    if (player) {
                                        if (player.getPlayerState() === 1) player.pauseVideo();
                                        else player.playVideo();
                                    }
                                }}
                                className="p-3 rounded-full bg-teal-500/20 text-teal-400 hover:bg-teal-500 hover:text-white transition-all scale-100 hover:scale-105"
                                title="Play/Pause (Space)"
                            >
                                {player && player.getPlayerState?.() === 1 ? <Pause className="w-5 h-5 fill-current" /> : <Play className="w-5 h-5 fill-current" />}
                            </button>

                            {/* Next Sentence */}
                            <button
                                onClick={() => {
                                    window.dispatchEvent(new KeyboardEvent('keydown', { key: 'ArrowRight' }));
                                }}
                                className="p-2 rounded-full hover:bg-white/10 text-gray-400 hover:text-white transition-colors"
                                title="Next Sentence (Right Arrow)"
                            >
                                <SkipForward className="w-5 h-5" />
                            </button>
                        </div>

                        <div className="flex items-center gap-4">
                            {/* Loop Toggle */}
                            <button
                                onClick={() => setIsLooping(!isLooping)}
                                className={`flex items-center gap-2 px-3 py-1.5 rounded-lg transition-all border ${isLooping ? 'bg-teal-500 text-white border-teal-400 shadow-[0_0_10px_rgba(20,184,166,0.5)]' : 'bg-transparent text-gray-400 border-white/10 hover:border-white/30'}`}
                                title="Toggle Single Sentence Loop (R)"
                            >
                                <Repeat className={`w-4 h-4 ${isLooping ? 'animate-spin-slow' : ''}`} />
                                <span className="text-sm font-medium hidden md:inline">{isLooping ? 'Looping' : 'Loop'}</span>
                            </button>
                        </div>
                    </div>

                    {/* Subtitles Layer (Bottom 35%, Dedicated Area) */}
                    <div
                        className="flex-1 bg-[#111] relative overflow-hidden" // Changed from h-35%
                        onMouseEnter={() => setIsHoveringList(true)}
                        onMouseLeave={() => setIsHoveringList(false)}
                    >
                        <div ref={scrollContainerRef} className="absolute inset-0 overflow-y-auto no-scrollbar scroll-smooth p-6 space-y-3">
                            {/* Mask gradient for smooth fade at top/bottom */}
                            <div className="sticky top-0 h-4 bg-gradient-to-b from-[#111] to-transparent z-10 pointer-events-none mb-[-1rem]"></div>

                            {transcriptData.map((item, idx) => {
                                const adjustedStart = item.start + syncOffset;
                                const adjustedEnd = item.end + syncOffset;
                                const isActive = currentTime >= adjustedStart && currentTime <= adjustedEnd;

                                return (
                                    <div
                                        key={idx}
                                        ref={isActive ? activeItemRef : null}
                                        onMouseEnter={() => handleLineHover(item)}
                                        onClick={() => seekTo(adjustedStart)}
                                        className={`group transition-all duration-300 rounded-lg p-3 cursor-pointer border flex flex-col items-center justify-center relative
                                            ${isActive
                                                ? 'bg-teal-500/10 border-teal-500/30 shadow-md shadow-teal-900/10 py-5'
                                                : 'hover:bg-white/5 border-transparent opacity-60 hover:opacity-100'
                                            }`}
                                    >
                                        <div className="text-center max-w-2xl mx-auto w-full">
                                            <div className="flex items-center justify-center gap-2 mb-1">
                                                <p className={`text-lg md:text-xl font-medium transition-colors text-center
                                                    ${isActive ? 'text-teal-200' : 'text-gray-300 group-hover:text-white'}`}>
                                                    {item.text_source_ruby ? (
                                                        <span dangerouslySetInnerHTML={{ __html: item.text_source_ruby }} />
                                                    ) : (
                                                        item.text_source
                                                    )}
                                                </p>
                                                {/* Replay Icon */}
                                                <button className="opacity-0 group-hover:opacity-100 p-1.5 rounded-full bg-white/10 hover:bg-teal-500 text-white transition-all transform scale-75">
                                                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><polygon points="5 3 19 12 5 21 5 3"></polygon></svg>
                                                </button>
                                            </div>
                                            <p className={`text-sm md:text-base transition-colors ${isActive ? 'text-teal-400/80' : 'text-gray-500 group-hover:text-gray-400'}`}>
                                                {item.text_target || (isActive ? "Thinking..." : "")}
                                            </p>
                                        </div>
                                    </div>
                                );
                            })}
                            <div className="h-12 w-full"></div> {/* Bottom Spacer */}
                        </div>
                    </div>
                </div>

                {/* ID: Sidebar (Deep Context) */}
                <div className="w-full md:w-[400px] bg-[#1c1c1e] border-l border-white/10 flex flex-col shrink-0 shadow-2xl z-10 transition-transform duration-300 h-[50vh] md:h-auto border-t md:border-t-0">
                    <div className="p-6 border-b border-white/10 bg-[#252527]">
                        <div className="flex items-center justify-between mb-2">
                            <div className="flex items-center gap-2">
                                <Sparkles className="w-4 h-4 text-teal-400" />
                                <span className="text-xs font-bold text-teal-400 uppercase tracking-widest">Deep Context</span>
                            </div>

                            {/* Sync Control (Sidebar) */}
                            <div className="flex items-center gap-1 bg-black/20 rounded-lg p-1">
                                <button onClick={() => adjustSync(-0.5)} className="w-5 h-5 flex items-center justify-center rounded hover:bg-teal-500/20 text-gray-400 hover:text-teal-400 text-xs">-</button>
                                <span className={`text-[10px] w-8 text-center font-mono ${syncOffset !== 0 ? 'text-teal-400 font-bold' : 'text-gray-500'}`}>
                                    {syncOffset > 0 ? '+' : ''}{syncOffset}s
                                </span>
                                <button onClick={() => adjustSync(0.5)} className="w-5 h-5 flex items-center justify-center rounded hover:bg-teal-500/20 text-gray-400 hover:text-teal-400 text-xs">+</button>
                            </div>
                        </div>
                        <p className="text-xs text-gray-400">
                            Hover words to learn. Adjust sync if needed.
                        </p>
                    </div>

                    <div className="flex-1 p-6 overflow-y-auto bg-[#1c1c1e]">
                        {activeContext ? (
                            <div className="animate-in slide-in-from-right-4 fade-in duration-300 space-y-6">
                                {
                                    /* 1. The Contextual Sentence */}
                                <div className="bg-teal-500/10 border border-teal-500/20 rounded-xl p-4">
                                    <Quote className="w-4 h-4 text-teal-400 mb-2 opacity-50" />
                                    <p className="text-lg text-white font-medium mb-1">
                                        {activeContext.text_source_ruby ? (
                                            <span dangerouslySetInnerHTML={{ __html: activeContext.text_source_ruby }} />
                                        ) : (
                                            activeContext.source
                                        )}
                                    </p>
                                    <p className="text-sm text-gray-400">
                                        {activeContext.target}
                                    </p>
                                </div>

                                {/* 2. Analysis Cards */}
                                <div className="space-y-4">
                                    {/* Summary/Type */}
                                    <div className="flex items-start gap-3">
                                        <div className="mt-1 w-1 h-full bg-blue-500 rounded-full min-h-[20px]"></div>
                                        <div>
                                            <span className="text-xs font-bold text-blue-400 uppercase">Context</span>
                                            <p className="text-gray-300 text-sm mt-1 leading-relaxed">
                                                {activeContext.summary || "No summary available."}
                                            </p>
                                        </div>
                                    </div>

                                    {/* Vocabulary */}
                                    {activeContext.vocab && activeContext.vocab.length > 0 && (
                                        <div>
                                            <span className="text-xs font-bold text-emerald-400 uppercase mb-3 block">Key Vocabulary</span>
                                            <div className="grid gap-3">
                                                {activeContext.vocab.map((v: any, i: number) => (
                                                    <div key={i} className={`p-4 rounded-xl border transition-all ${v.highlight ? 'bg-amber-400/10 border-amber-400/30' : 'bg-white/5 border-white/5'}`}>
                                                        <div className="flex items-center justify-between mb-2">
                                                            <div className="flex items-baseline gap-2">
                                                                <span className="font-bold text-lg text-gray-100">{v.word}</span>
                                                                {v.ipa && <span className="text-gray-500 font-mono text-xs">{v.ipa}</span>}

                                                                {/* TTS Button */}
                                                                <button
                                                                    onClick={(e) => {
                                                                        e.stopPropagation();
                                                                        speakWord(v.word);
                                                                    }}
                                                                    className="p-1.5 rounded-full bg-white/5 hover:bg-green-500 text-gray-400 hover:text-black transition-all"
                                                                    title="Pronounce"
                                                                >
                                                                    <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"></polygon><path d="M19.07 4.93a10 10 0 0 1 0 14.14M15.54 8.46a5 5 0 0 1 0 7.07"></path></svg>
                                                                </button>
                                                            </div>
                                                            <div className="flex items-center gap-2">
                                                                {v.highlight && <span className="text-[10px] bg-amber-400 text-black px-1.5 py-0.5 rounded font-bold uppercase">Focus</span>}

                                                                <button
                                                                    onClick={(e) => {
                                                                        e.stopPropagation();
                                                                        handleSaveVocab(v.word, v.meaning);
                                                                    }}
                                                                    className={`p-1.5 rounded-full transition-all ${savedVocabs.has(v.word) ? 'bg-red-500/20 text-red-500' : 'bg-white/5 text-gray-400 hover:text-red-500 hover:bg-red-500/10'}`}
                                                                    title="Save to Vocab"
                                                                >
                                                                    <Heart className={`w-4 h-4 ${savedVocabs.has(v.word) ? 'fill-current' : ''}`} />
                                                                </button>
                                                            </div>
                                                        </div>

                                                        {v.pos && <div className="text-xs text-green-400 font-semibold mb-1 italic">{v.pos}</div>}
                                                        <p className="text-sm text-gray-300 mb-2">{v.meaning}</p>
                                                        {v.definition_en && (
                                                            <div className="text-xs text-gray-500 border-l-2 border-white/10 pl-2 mb-2 italic leading-relaxed">"{v.definition_en}"</div>
                                                        )}

                                                        {/* Rich Details: Synonyms & Phrases */}
                                                        {((v.synonyms && v.synonyms.length > 0) || (v.common_phrases && v.common_phrases.length > 0)) && (
                                                            <div className="mt-3 pt-3 border-t border-white/5 space-y-2">
                                                                {v.synonyms && v.synonyms.length > 0 && (
                                                                    <div className="flex flex-wrap gap-1.5 items-center">
                                                                        <span className="text-[10px] text-gray-600 uppercase">Syn:</span>
                                                                        {v.synonyms.map((syn: string, si: number) => (
                                                                            <span key={si} className="text-xs bg-white/10 px-1.5 py-0.5 rounded text-gray-400">{syn}</span>
                                                                        ))}
                                                                    </div>
                                                                )}
                                                                {v.common_phrases && v.common_phrases.length > 0 && (
                                                                    <div className="flex flex-col gap-1">
                                                                        <span className="text-[10px] text-gray-600 uppercase">Phrases:</span>
                                                                        {v.common_phrases.map((ph: string, pi: number) => (
                                                                            <span key={pi} className="text-xs text-teal-200">• {ph}</span>
                                                                        ))}
                                                                    </div>
                                                                )}
                                                            </div>
                                                        )}
                                                    </div>
                                                ))}
                                            </div>
                                        </div>
                                    )}

                                    {/* Grammar / Culture */}
                                    {(activeContext.grammar || activeContext.cultural_note) && (
                                        <div className="bg-white/5 rounded-xl p-4 space-y-4">
                                            {activeContext.grammar && (
                                                <div>
                                                    <span className="text-xs font-bold text-orange-400 uppercase block mb-1">Grammar Point</span>
                                                    <p className="text-sm text-gray-300">{activeContext.grammar}</p>
                                                </div>
                                            )}
                                            {activeContext.cultural_note && (
                                                <div>
                                                    <span className="text-xs font-bold text-pink-400 uppercase block mb-1">Cultural Note</span>
                                                    <p className="text-sm text-gray-300">{activeContext.cultural_note}</p>
                                                </div>
                                            )}
                                        </div>
                                    )}
                                </div>
                            </div>
                        ) : (
                            <div className="h-full flex flex-col items-center justify-center text-gray-600 text-center space-y-4 p-8 opacity-50">
                                <BookOpen className="w-12 h-12 mb-2" />
                                <p>Hover over a subtitle line to see the Magic Context.</p>
                            </div>
                        )}
                    </div>
                </div>
            </div>
        </div >
    );
}
