'use client';

import { useState, useEffect, useRef } from 'react';
import { useRouter } from 'next/navigation';
import YouTube from 'react-youtube';
import { FRIENDS_QUIZ_DATA, QuizQuestion, PersonaType } from '@/lib/friends_data';
import Link from 'next/link';

export default function FriendsPlay() {
    const router = useRouter();
    const [currentQIndex, setCurrentQIndex] = useState(0);
    const [gameState, setGameState] = useState<'WATCHING' | 'QUESTION' | 'FEEDBACK'>('WATCHING');
    const [player, setPlayer] = useState<any>(null);
    const [scores, setScores] = useState<Record<string, number>>({ Joey: 0, Monica: 0, Ross: 0, Chandler: 0, Rachel: 0, Phoebe: 0 });
    const [selectedOption, setSelectedOption] = useState<number | null>(null);

    const question = FRIENDS_QUIZ_DATA[currentQIndex];

    if (!question) {
        return <div className="h-screen bg-black text-white flex items-center justify-center">Loading Data...</div>;
    }

    const onReady = (event: any) => {
        setPlayer(event.target);
        // Start playing segment
        playSegment(event.target);
    };

    const playSegment = (ytPlayer: any) => {
        if (!ytPlayer) return;
        ytPlayer.seekTo(question.clipStart, true);
        ytPlayer.playVideo();
        setGameState('WATCHING');
    };

    // Monitor time to stop for question
    useEffect(() => {
        let interval: NodeJS.Timeout;
        if (player && gameState === 'WATCHING') {
            interval = setInterval(() => {
                const t = player.getCurrentTime();
                if (t >= question.clipEnd) {
                    player.pauseVideo();
                    setGameState('QUESTION');
                }
            }, 500);
        }
        return () => clearInterval(interval);
    }, [player, gameState, question]);

    const handleAnswer = (optionIdx: number) => {
        setSelectedOption(optionIdx);
        setGameState('FEEDBACK');

        const option = question.options[optionIdx];

        // Update Persona Score
        setScores(prev => ({
            ...prev,
            [option.persona]: (prev[option.persona] || 0) + 1
        }));
    };

    const [showSubs, setShowSubs] = useState(false);

    const nextQuestion = () => {
        if (currentQIndex < FRIENDS_QUIZ_DATA.length - 1) {
            // DO NOT setPlayer(null) here; we need to reuse the instance
            setIsPlaying(false); // Reset Play State
            setShowSubs(false); // Reset Subs to hidden
            setCurrentQIndex(currentQIndex + 1);
            setGameState('WATCHING');
            setSelectedOption(null);
        } else {
            // End Game -> Result
            // Serialize scores to URL or context? URL is viral.
            const query = new URLSearchParams();
            Object.entries(scores).forEach(([k, v]) => query.set(k, v.toString()));
            router.push(`/friends/result?${query.toString()}`);
        }
    };

    // Load new video when question changes
    useEffect(() => {
        if (player && question) {
            setGameState('WATCHING');
            setIsPlaying(true);
            // We rely on 'key' prop to remount component, but we also ensure state is reset
        }
    }, [currentQIndex, player]);

    const [isPlaying, setIsPlaying] = useState(false);

    const onStateChange = (event: any) => {
        setIsPlaying(event.data === 1);
    };

    return (
        <div className="h-screen bg-black flex flex-col items-center justify-center relative overflow-hidden font-sans">
            {/* Header / Progress */}
            <div className="absolute top-4 left-0 w-full z-20 px-6 flex justify-between items-center text-white/50 text-sm font-bold uppercase tracking-widest">
                <span>The One With The Quiz</span>
                <span>{currentQIndex + 1} / {FRIENDS_QUIZ_DATA.length}</span>
            </div>

            {/* Video Background/Player */}
            <div className={`w-full h-full pointer-events-none transition-filter duration-500 ${gameState === 'WATCHING' ? '' : 'blur-md opacity-50'}`}>
                <YouTube
                    key={question.videoId} // RESTORE KEY: Forces remount on new video (Most Stable)
                    videoId={question.videoId}
                    className="w-full h-full"
                    iframeClassName="w-full h-full object-cover"
                    onReady={onReady}
                    onStateChange={onStateChange}
                    opts={{
                        playerVars: {
                            controls: 0,
                            showinfo: 0,
                            rel: 0,
                            modestbranding: 1,
                            cc_load_policy: 0,
                            fs: 0,
                            start: question.clipStart,
                            end: question.clipEnd // Also adding end just in case, though we have manual interval
                        }
                    }}
                />

                {/* Toggle Subtitles Button */}
                {gameState === 'WATCHING' && (
                    <button
                        onClick={() => setShowSubs(!showSubs)}
                        className="absolute top-24 right-6 z-50 pointer-events-auto bg-white/20 hover:bg-white/30 backdrop-blur-md text-white px-5 py-2 rounded-full text-sm font-bold border border-white/40 transition-all flex items-center gap-2 transform active:scale-95 shadow-lg"
                    >
                        <span>{showSubs ? '🙈 Hide' : '👀 Peek Answer'}</span>
                    </button>
                )}

                {/* Custom Subtitles Overlay */}
                {((gameState === 'WATCHING' && showSubs) || gameState === 'FEEDBACK') && question.subs && (
                    <div className="absolute bottom-20 left-0 w-full text-center px-4 z-20 animate-in fade-in slide-in-from-bottom-5 duration-500">
                        <div className="inline-block bg-black/60 backdrop-blur-sm px-6 py-3 rounded-2xl border border-[#F2C94C]/30 shadow-2xl">
                            <p className="text-[#F2C94C] text-xs uppercase font-bold tracking-widest mb-1">
                                The Iconic Line
                            </p>
                            <p className="text-white text-lg md:text-2xl font-bold shadow-black drop-shadow-md mb-1">
                                "{question.subs.en}"
                            </p>
                            <p className="text-gray-300 text-sm md:text-base font-medium">
                                {question.subs.zh}
                            </p>
                        </div>
                    </div>
                )}
            </div>

            {/* Manual Play Button (Fix for Autoplay Block) */}
            {gameState === 'WATCHING' && !isPlaying && (
                <div className="absolute inset-0 z-30 flex items-center justify-center bg-black/20 backdrop-blur-[2px]">
                    <button
                        onClick={() => player?.playVideo()}
                        className="bg-[#F2C94C] hover:bg-[#d9b442] text-black w-20 h-20 rounded-full flex items-center justify-center shadow-2xl transition-transform hover:scale-110 animate-bounce"
                    >
                        <svg className="w-10 h-10 ml-1" fill="currentColor" viewBox="0 0 24 24">
                            <path d="M8 5v14l11-7z" />
                        </svg>
                    </button>
                    <p className="absolute mt-28 text-white font-bold tracking-widest uppercase text-sm shadow-black drop-shadow-md">
                        Tap to Start Scene
                    </p>
                </div>
            )}

            {/* Overlay: Question */}
            {gameState !== 'WATCHING' && (
                <div className="absolute inset-0 z-10 flex flex-col items-center justify-center p-6 bg-black/40 backdrop-blur-sm animate-in fade-in zoom-in-95 duration-300">
                    <div className="bg-[#1e1e1e] border-2 border-[#F2C94C] p-8 rounded-2xl max-w-lg w-full shadow-2xl">

                        <h2 className="text-2xl text-white font-bold mb-6 text-center leading-tight">
                            {question.question}
                        </h2>

                        <div className="space-y-3">
                            {question.options.map((opt, i) => {
                                const isSelected = selectedOption === i;
                                const showResult = gameState === 'FEEDBACK';

                                let btnClass = "w-full p-4 rounded-xl text-left font-medium transition-all transform hover:scale-[1.02] active:scale-95 border-2 ";

                                if (showResult) {
                                    if (isSelected) {
                                        // Selected Item: Show Theme Purple
                                        btnClass += "bg-[#7B538C] border-[#9b6fac] text-white shadow-[0_0_15px_rgba(123,83,140,0.5)]";
                                    } else {
                                        // Unselected: Fade out
                                        btnClass += "bg-[#2a2a2a] border-transparent text-gray-600 opacity-40 grayscale";
                                    }
                                } else {
                                    // Default State
                                    btnClass += "bg-[#2a2a2a] border-transparent hover:bg-[#333] hover:border-[#F2C94C]/50 text-gray-200";
                                }
                                return (
                                    <button
                                        key={i}
                                        disabled={showResult}
                                        onClick={() => handleAnswer(i)}
                                        className={btnClass}
                                    >
                                        <div className="flex justify-between items-center">
                                            <span>{opt.text}</span>
                                            {showResult && isSelected && (
                                                <span className="text-xs uppercase font-bold tracking-wider bg-white/20 px-2 py-1 rounded">
                                                    + {opt.persona}
                                                </span>
                                            )}
                                        </div>
                                    </button>
                                );
                            })}
                        </div>

                        {/* Feedback / Next */}
                        {gameState === 'FEEDBACK' && selectedOption !== null && (
                            <div className="mt-6 pt-6 border-t border-white/10 text-center animate-in slide-in-from-bottom-2">
                                <p className="text-[#F2C94C] italic font-medium mb-4">
                                    "{question.options[selectedOption].feedback}"
                                </p>
                                <button
                                    onClick={nextQuestion}
                                    className="bg-[#7B538C] hover:bg-[#6a467a] text-white px-8 py-3 rounded-full font-bold uppercase tracking-widest shadow-lg transition-transform hover:scale-105"
                                >
                                    {currentQIndex < FRIENDS_QUIZ_DATA.length - 1 ? "Next Scene" : "Finish"}
                                </button>
                            </div>
                        )}
                    </div>
                </div>
            )}
        </div>
    );
}
