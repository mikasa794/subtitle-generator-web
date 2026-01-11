'use client';

import { useState } from 'react';
import { useRouter } from 'next/navigation';
import { FRIENDS_WRITTEN_DATA } from '@/lib/friends_written_data';

export default function WrittenExam() {
    const router = useRouter();
    const [currentIndex, setCurrentIndex] = useState(0);
    const [scores, setScores] = useState<Record<string, number>>({});
    const [lastFeedback, setLastFeedback] = useState<{ en: string; zh: string } | null>(null);

    const question = FRIENDS_WRITTEN_DATA[currentIndex];
    const progress = ((currentIndex) / FRIENDS_WRITTEN_DATA.length) * 100;

    const handleAnswer = (option: any) => {
        // Record Score
        setScores(prev => ({
            ...prev,
            [option.persona]: (prev[option.persona] || 0) + 1
        }));
        setLastFeedback(option.feedback);
    };

    const handleNext = () => {
        setLastFeedback(null);
        if (currentIndex < FRIENDS_WRITTEN_DATA.length - 1) {
            setCurrentIndex(currentIndex + 1);
        } else {
            // Finish
            const query = new URLSearchParams();
            Object.entries(scores).forEach(([k, v]) => query.set(k, v.toString()));
            router.push(`/friends/result?${query.toString()}`);
        }
    };

    return (
        <div className="min-h-screen bg-[#F5F5F5] text-gray-900 font-sans flex flex-col items-center justify-center p-6 relative overflow-hidden">
            {/* Background Patterns */}
            <div className="absolute inset-0 opacity-5 pointer-events-none" style={{ backgroundImage: 'radial-gradient(circle, #000 1px, transparent 1px)', backgroundSize: '20px 20px' }}></div>

            {/* Header */}
            <div className="w-full max-w-2xl flex justify-between items-center mb-8 z-10">
                <h1 className="text-2xl font-extrabold tracking-tighter text-[#7B538C]">
                    THE ONE WITH THE TEXT
                </h1>
                <div className="text-xs font-bold uppercase tracking-widest text-gray-400">
                    {currentIndex + 1} / {FRIENDS_WRITTEN_DATA.length}
                </div>
            </div>

            {/* Progress Bar */}
            <div className="w-full max-w-2xl h-2 bg-gray-200 rounded-full mb-12 overflow-hidden z-10">
                <div
                    className="h-full bg-[#F2C94C] transition-all duration-500 ease-out"
                    style={{ width: `${progress}%` }}
                ></div>
            </div>

            {/* Card */}
            <div className="bg-white w-full max-w-2xl p-8 md:p-12 rounded-3xl shadow-2xl border-b-8 border-[#7B538C] relative z-10 animate-in zoom-in-95 duration-300">

                {/* Feedback Overlay (Manual Next) */}
                {lastFeedback ? (
                    <div className="absolute inset-0 bg-[#F2C94C] rounded-2xl flex flex-col items-center justify-center p-8 z-20 animate-in fade-in zoom-in-100 text-center">
                        <h2 className="text-2xl md:text-3xl font-black text-black leading-tight mb-2">
                            "{lastFeedback.en}"
                        </h2>
                        <p className="text-lg md:text-xl font-medium text-black/80 mb-8">
                            {lastFeedback.zh}
                        </p>

                        <button
                            onClick={handleNext}
                            className="bg-black text-white px-8 py-3 rounded-full font-bold uppercase tracking-widest hover:bg-gray-800 transition-transform hover:scale-105 shadow-xl"
                        >
                            Continue -&gt;
                        </button>
                    </div>
                ) : (
                    <>
                        <div className="mb-8">
                            <h2 className="text-2xl md:text-3xl font-bold leading-tight text-gray-800 mb-2">
                                {question.scenario.en}
                            </h2>
                            <p className="text-gray-500 font-medium text-lg">
                                {question.scenario.zh}
                            </p>
                        </div>

                        <div className="grid grid-cols-1 gap-4">
                            {question.options.map((opt, i) => (
                                <button
                                    key={i}
                                    onClick={() => handleAnswer(opt)}
                                    className="text-left p-6 rounded-xl border-2 border-gray-100 hover:border-[#7B538C] hover:bg-[#7B538C]/5 transition-all group flex flex-col"
                                >
                                    <div className="flex items-center mb-1">
                                        <span className="font-bold text-gray-400 mr-4 group-hover:text-[#7B538C]">{String.fromCharCode(65 + i)}.</span>
                                        <span className="font-medium text-lg text-gray-700 group-hover:text-black">{opt.text.en}</span>
                                    </div>
                                    <span className="text-sm text-gray-400 pl-8 group-hover:text-gray-600">{opt.text.zh}</span>
                                </button>
                            ))}
                        </div>
                    </>
                )}
            </div>

            <p className="mt-8 text-gray-400 text-xs text-center max-w-md z-10">
                *There are no wrong answers, only different levels of Neuroticism.
            </p>
        </div>
    );
}
