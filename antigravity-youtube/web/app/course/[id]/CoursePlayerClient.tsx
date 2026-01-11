'use client';

import { useState, useEffect, useRef } from 'react';
import YouTube from 'react-youtube';
import { Play, Sparkles, BookOpen, Quote } from 'lucide-react';

interface Props {
    title: string;
    videoUrl: string;
    transcript: string;
}

interface TranscriptItem {
    start: number;
    end: number;
    text_source: string;
    text_target: string;
    context?: {
        type: string;
        summary?: string;
        grammar?: string;
        cultural_note?: string;
        vocab?: any[];
    };
}

export default function CoursePlayerClient({ title, videoUrl, transcript }: Props) {
    const [player, setPlayer] = useState<any>(null);
    const [transcriptData, setTranscriptData] = useState<TranscriptItem[]>([]);
    const [isJsonTranscript, setIsJsonTranscript] = useState(false);

    // Playback State
    const [currentTime, setCurrentTime] = useState(0);
    const [activeContext, setActiveContext] = useState<any>(null);

    // 1. Parse Transcript
    useEffect(() => {
        if (!transcript) {
            setTranscriptData([]);
            return;
        }

        try {
            const parsed = JSON.parse(transcript);
            if (Array.isArray(parsed) && parsed.length > 0 && parsed[0].start !== undefined) {
                setTranscriptData(parsed);
                setIsJsonTranscript(true);
                return;
            }
        } catch (e) { }

        // Legacy Text Parsing
        const lines = transcript.split('\n').filter(line => line.trim() !== '');
        const parsedLegacy = lines.map(line => {
            const match = line.match(/\[(\d+):(\d+)\]\s*(.*)/);
            if (match) {
                const min = parseInt(match[1], 10);
                const sec = parseInt(match[2], 10);
                return {
                    start: min * 60 + sec,
                    end: min * 60 + sec + 5,
                    text_source: match[3],
                    text_target: '',
                };
            }
            return { start: 0, end: 5, text_source: line, text_target: '' };
        });
        setTranscriptData(parsedLegacy);
        setIsJsonTranscript(false);
    }, [transcript]);

    // 2. Timer Loop
    useEffect(() => {
        let interval: NodeJS.Timeout;
        if (player) {
            interval = setInterval(() => {
                const t = player.getCurrentTime();
                setCurrentTime(t);
            }, 100);
        }
        return () => clearInterval(interval);
    }, [player]);

    const speakWord = (word: string) => {
        const utterance = new SpeechSynthesisUtterance(word);
        utterance.lang = 'en-US';
        window.speechSynthesis.speak(utterance);
    };

    const getYouTubeId = (url: string) => {
        const regExp = /^.*(youtu.be\/|v\/|u\/\w\/|embed\/|watch\?v=|&v=)([^#&?]*).*/;
        const match = url?.match(regExp);
        return (match && match[2].length === 11) ? match[2] : null;
    };
    const videoId = getYouTubeId(videoUrl);

    const onReady = (event: any) => {
        setPlayer(event.target);
    };

    const seekTo = (seconds: number) => {
        if (player) {
            player.seekTo(seconds, true);
            player.playVideo();
        }
    };

    const handleLineHover = (item: TranscriptItem) => {
        if (item.context) {
            setActiveContext({
                ...item.context,
                source: item.text_source,
                target: item.text_target
            });
        }
    };

    return (
        <div className="flex flex-col gap-8 font-sans">
            {/* Header */}
            <div>
                <h2 className="text-3xl font-semibold text-[#1d1d1f] mb-2">{title}</h2>
                <div className="flex gap-2 text-sm text-gray-500 items-center">
                    <span className="bg-blue-100 text-blue-700 px-2 py-0.5 rounded text-xs font-bold">LESSON</span>
                    {isJsonTranscript && <span className="bg-teal-100 text-teal-700 px-2 py-0.5 rounded text-xs font-bold flex items-center gap-1"><Sparkles className="w-3 h-3" /> AI ENHANCED</span>}
                </div>
            </div>

            {/* Main Content Area */}
            <div className="flex flex-col lg:flex-row gap-8 items-start">

                {/* Visual Area: Video + Overlay (Larger) */}
                <div className="flex-[3] w-full bg-black rounded-[24px] overflow-hidden shadow-2xl relative group aspect-video flex flex-col justify-center min-w-0">
                    {videoId ? (
                        <>
                            <div className="absolute inset-0 z-0">
                                <YouTube
                                    videoId={videoId}
                                    className="w-full h-full"
                                    iframeClassName="w-full h-full"
                                    onReady={onReady}
                                    opts={{
                                        playerVars: {
                                            autoplay: 0,
                                            controls: 1,
                                            cc_load_policy: 0,
                                            rel: 0,
                                            modestbranding: 1
                                        }
                                    }}
                                />
                            </div>

                            {/* Overlay Subtitles Container - Smaller Font, Better Position */}
                            <div className="absolute bottom-12 left-0 right-0 z-10 px-8 pointer-events-none flex flex-col items-center justify-end text-center transition-opacity">
                                {transcriptData.map((item, idx) => {
                                    const isActive = currentTime >= item.start && currentTime <= item.end;
                                    if (!isActive) return null;

                                    return (
                                        <div key={idx}
                                            className="pointer-events-auto bg-black/70 backdrop-blur-sm px-4 py-2 rounded-xl mb-6 hover:bg-black/90 transition-all cursor-pointer transform hover:scale-105 border border-white/10 shadow-lg max-w-3xl"
                                            onMouseEnter={() => handleLineHover(item)}>
                                            <p className="text-white text-lg md:text-xl font-bold leading-relaxed drop-shadow-md tracking-wide">
                                                {item.text_source}
                                            </p>
                                            {item.text_target && (
                                                <p className="text-teal-200 text-sm md:text-base mt-1 font-normal opacity-90 drop-shadow-sm">
                                                    {item.text_target}
                                                </p>
                                            )}
                                        </div>
                                    );
                                })}
                            </div>
                        </>
                    ) : (
                        <div className="w-full h-full flex items-center justify-center text-gray-500">Video URL missing</div>
                    )}
                </div>

                {/* Sidebar: Deep Context (Persistent) */}
                <div className="w-full lg:w-[320px] bg-[#1c1c1e] text-white rounded-2xl overflow-hidden flex flex-col shadow-xl shrink-0 border border-white/5 h-[500px] lg:h-auto lg:aspect-[9/16] xl:aspect-[3/4]">
                    <div className="p-5 border-b border-white/10 bg-[#252527] flex items-center gap-3">
                        <Sparkles className="w-5 h-5 text-teal-400" />
                        <span className="font-bold text-sm uppercase tracking-widest text-teal-400">
                            Deep Context: {activeContext?.type ? activeContext.type.charAt(0).toUpperCase() + activeContext.type.slice(1) : (isJsonTranscript ? "Ready" : "Waiting")}
                        </span>
                    </div>

                    <div className="flex-1 p-6 overflow-y-auto custom-scrollbar bg-[#1c1c1e]">
                        {activeContext ? (
                            <div className="space-y-6 animate-in fade-in slide-in-from-right-4 duration-300">
                                {/* Source Quote */}
                                <div className="bg-gradient-to-br from-teal-500/10 to-teal-900/10 rounded-xl p-4 border border-teal-500/20">
                                    <Quote className="w-6 h-6 text-teal-500 mb-3 opacity-50" />
                                    <p className="text-lg font-medium text-white mb-2 leading-relaxed font-serif">{activeContext.source}</p>
                                    <p className="text-sm text-gray-400 font-light">{activeContext.target}</p>
                                </div>

                                {/* Summary / Analysis */}
                                {activeContext.summary && (
                                    <div>
                                        <h4 className="text-xs font-bold text-blue-400 uppercase tracking-wider mb-2">Analysis</h4>
                                        <p className="text-gray-300 text-sm leading-relaxed bg-white/5 p-3 rounded-lg border border-white/5">
                                            {activeContext.summary}
                                        </p>
                                    </div>
                                )}

                                {/* Vocab / Concepts */}
                                {activeContext.vocab && activeContext.vocab.length > 0 && (
                                    <div>
                                        <h4 className="text-xs font-bold text-emerald-400 uppercase tracking-wider mb-3">
                                            {activeContext.type === 'tech' ? 'Key Concepts' : 'Vocabulary'}
                                        </h4>
                                        <div className="space-y-3">
                                            {activeContext.vocab.map((v: any, i: number) => (
                                                <div key={i} className="bg-white/5 rounded-xl p-3 border border-white/5 hover:bg-white/10 transition-colors group cursor-help">
                                                    <div className="flex justify-between items-start mb-1">
                                                        <span className="font-bold text-teal-100 text-base">{v.word}</span>
                                                        <button onClick={(e) => { e.stopPropagation(); speakWord(v.word); }} className="text-gray-500 hover:text-white opacity-0 group-hover:opacity-100 transition-opacity p-1">
                                                            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"></polygon><path d="M19.07 4.93a10 10 0 0 1 0 14.14M15.54 8.46a5 5 0 0 1 0 7.07"></path></svg>
                                                        </button>
                                                    </div>
                                                    <p className="text-sm text-gray-400 leading-relaxed">{v.meaning}</p>
                                                </div>
                                            ))}
                                        </div>
                                    </div>
                                )}
                            </div>
                        ) : (
                            <div className="h-full flex flex-col items-center justify-center text-gray-500 text-center space-y-6 px-4">
                                {isJsonTranscript ? (
                                    <>
                                        <div className="w-16 h-16 rounded-full bg-white/5 flex items-center justify-center mb-2">
                                            <BookOpen className="w-8 h-8 opacity-50" />
                                        </div>
                                        <p className="text-base font-medium text-gray-400">Hover over subtitles to reveal insights.</p>
                                    </>
                                ) : (
                                    <>
                                        <div className="w-12 h-12 rounded-full border-2 border-t-teal-500 border-r-transparent border-b-gray-700 border-l-transparent animate-spin mb-2"></div>
                                        <div>
                                            <p className="text-sm font-medium text-gray-300">Generating Context...</p>
                                            <p className="text-xs text-gray-600 mt-1">AI agent is processing this lesson.</p>
                                        </div>
                                    </>
                                )}
                            </div>
                        )}
                    </div>
                </div>
            </div>

            {/* Bottom: Full Transcript */}
            <div className="border-t border-gray-200 mt-4 pt-8">
                <h3 className="text-lg font-semibold mb-4 text-[#1d1d1f]">Transcript</h3>
                <div className="bg-gray-50 rounded-2xl p-6 h-[300px] overflow-y-auto space-y-1 custom-scrollbar">
                    {transcriptData.map((item, idx) => (
                        <div key={idx}
                            onClick={() => seekTo(item.start)}
                            className={`cursor-pointer hover:bg-gray-200 px-4 py-2 rounded-lg flex gap-4 transition-colors ${currentTime >= item.start && currentTime <= item.end ? 'bg-blue-100/50 text-blue-900 font-medium sticky top-0 bottom-0 z-10 backdrop-blur-sm' : 'text-gray-600'}`}>
                            <span className="font-mono text-xs opacity-50 pt-1 w-12 shrink-0">{Math.floor(item.start / 60)}:{Math.floor(item.start % 60).toString().padStart(2, '0')}</span>
                            <div>
                                <p className="text-sm leading-relaxed font-medium text-gray-900">{item.text_source}</p>
                                {item.text_target && (
                                    <p className="text-xs leading-relaxed text-gray-500 mt-0.5">{item.text_target}</p>
                                )}
                            </div>
                        </div>
                    ))}
                </div>
            </div>
        </div>
    );
}
