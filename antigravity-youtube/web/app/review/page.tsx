'use client';

import { useState, useEffect } from 'react';
import Link from 'next/link';
import { ChevronLeft, Brain, Sparkles, Check, X, RotateCcw } from 'lucide-react';

interface VocabItem {
    id: string;
    word: string;
    meaning: string;
    context: string;
    videoTitle: string;
    videoUrl: string;
    timestamp: number;
}

export default function ReviewPage() {
    const [items, setItems] = useState<VocabItem[]>([]);
    const [loading, setLoading] = useState(true);
    const [currentIndex, setCurrentIndex] = useState(0);
    const [showResult, setShowResult] = useState(false);
    const [selectedOption, setSelectedOption] = useState<string | null>(null);
    const [options, setOptions] = useState<string[]>([]);

    useEffect(() => {
        fetch('/api/vocab/list')
            .then(res => res.json())
            .then(data => {
                if (data.success) {
                    setItems(data.items);
                }
                setLoading(false);
            })
            .catch(() => setLoading(false));
    }, []);

    // Generate Options when moving to new card
    useEffect(() => {
        if (items.length > 0 && items[currentIndex]) {
            generateOptions(items[currentIndex]);
            setShowResult(false);
            setSelectedOption(null);
        }
    }, [items, currentIndex]);

    const generateOptions = (current: VocabItem) => {
        // Correct Answer
        const correct = current.word;
        // Distractors: Randomly pick 3 others from list
        let pool = items.filter(i => i.id !== current.id).map(i => i.word);
        // Shuffle pool
        pool = pool.sort(() => 0.5 - Math.random());
        // Take 3
        const distractors = pool.slice(0, 3);
        // If not enough, fill with Friends-themed words
        const friendsWords = ["Unagi", "Pivot", "Sandwich", "Dinosaur", "Smelly Cat", "Lobster", "Break", "HowYouDoin"];
        let fallbackIdx = 0;
        while (distractors.length < 3) {
            distractors.push(friendsWords[fallbackIdx % friendsWords.length]);
            fallbackIdx++;
        }

        // Combine and Shuffle
        const all = [correct, ...distractors].sort(() => 0.5 - Math.random());
        setOptions(all);
    };

    const handleAnswer = (option: string) => {
        if (showResult) return;
        setSelectedOption(option);
        setShowResult(true);
    };

    const handleNext = () => {
        if (currentIndex < items.length - 1) {
            setCurrentIndex(prev => prev + 1);
        } else {
            // Loop or Finish
            alert("All done! Great job!");
            setCurrentIndex(0);
        }
    };

    if (loading) return <div className="min-h-screen bg-black text-white flex items-center justify-center">Loading your collection...</div>;

    if (items.length === 0) return (
        <div className="min-h-screen bg-black text-white flex flex-col items-center justify-center space-y-4">
            <Brain className="w-16 h-16 text-gray-600" />
            <p className="text-xl font-medium text-gray-400">Your collection is empty.</p>
            <p className="text-gray-500">Go watch some videos and save words!</p>
            <Link href="/lingo" className="text-teal-400 hover:underline">Go to Library</Link>
        </div>
    );

    const currentItem = items[currentIndex];
    // Create Cloze Sentence
    // Regex to replace word (case insensitive) with _______
    // Be careful with punctuation.
    const clozeSentence = currentItem.context ? currentItem.context.replace(new RegExp(currentItem.word, 'gi'), "_______") : "No context available.";

    return (
        <div className="min-h-screen bg-black text-white flex flex-col">
            {/* Header */}
            <header className="h-[60px] flex items-center px-6 border-b border-white/10 shrink-0">
                <Link href="/lingo" className="flex items-center gap-2 text-gray-400 hover:text-white transition-colors">
                    <ChevronLeft className="w-5 h-5" />
                    <span>Exit</span>
                </Link>
                <div className="ml-auto flex items-center gap-2 text-teal-400 font-bold">
                    <Brain className="w-5 h-5" />
                    <span>Review Mode</span>
                </div>
            </header>

            {/* Main Content */}
            <main className="flex-1 flex flex-col items-center justify-center p-6 max-w-2xl mx-auto w-full">

                {/* Progress */}
                <div className="w-full h-1 bg-white/10 rounded-full mb-8 overflow-hidden">
                    <div
                        className="h-full bg-gradient-to-r from-teal-500 to-blue-500 transition-all duration-300"
                        style={{ width: `${((currentIndex + 1) / items.length) * 100}%` }}
                    ></div>
                </div>

                {/* Card */}
                <div className="w-full bg-[#1c1c1e] border border-white/10 rounded-3xl p-8 md:p-12 shadow-2xl relative overflow-hidden group">
                    {/* Background decoration */}
                    <div className="absolute top-0 right-0 w-64 h-64 bg-teal-500/5 rounded-full blur-3xl -mr-32 -mt-32"></div>

                    {/* Context Question */}
                    <div className="relative z-10 text-center mb-12">
                        <QuoteIcon className="w-8 h-8 text-teal-500/30 mx-auto mb-6" />
                        <h2 className="text-2xl md:text-3xl font-serif leading-relaxed text-gray-200">
                            "{clozeSentence}"
                        </h2>
                        {currentItem.videoTitle && (
                            <p className="mt-4 text-sm text-gray-500 font-mono">
                                from: {currentItem.videoTitle}
                            </p>
                        )}
                    </div>

                    {/* Options Grid */}
                    <div className="grid grid-cols-1 md:grid-cols-2 gap-4 relative z-10 h-[200px]">
                        {/* Fixed height to prevent layout jump? Or dynamic? */}
                        {options.map((opt, i) => {
                            let stateClass = "bg-white/5 border-white/10 hover:bg-white/10 hover:border-white/30 text-gray-300";

                            if (showResult) {
                                if (opt === currentItem.word) {
                                    stateClass = "bg-green-500/20 border-green-500 text-green-400"; // Correct
                                } else if (opt === selectedOption) {
                                    stateClass = "bg-red-500/20 border-red-500 text-red-400"; // Wrong Selected
                                } else {
                                    stateClass = "opacity-30 bg-black/20 border-transparent"; // Others
                                }
                            }

                            return (
                                <button
                                    key={i}
                                    onClick={() => handleAnswer(opt)}
                                    disabled={showResult}
                                    className={`p-4 rounded-xl border text-lg font-medium transition-all duration-200 transform active:scale-95 ${stateClass}`}
                                >
                                    {opt}
                                </button>
                            );
                        })}
                    </div>

                    {/* Feedback Overlay / Next Button */}
                    {showResult && (
                        <div className="absolute inset-0 z-20 flex items-center justify-center bg-black/60 backdrop-blur-sm animate-in fade-in duration-300">
                            <div className="bg-[#252527] border border-white/20 p-8 rounded-2xl shadow-2xl text-center max-w-sm w-full mx-4 transform scale-100 animate-in zoom-in-95">
                                <div className={`w-16 h-16 mx-auto rounded-full flex items-center justify-center mb-4 ${selectedOption === currentItem.word ? 'bg-green-500/20 text-green-400' : 'bg-red-500/20 text-red-500'}`}>
                                    {selectedOption === currentItem.word ? <Check className="w-8 h-8" /> : <X className="w-8 h-8" />}
                                </div>
                                <h3 className="text-xl font-bold text-white mb-2">
                                    {selectedOption === currentItem.word ? 'Correct!' : 'Nice try!'}
                                </h3>
                                <p className="text-gray-400 mb-6">
                                    {selectedOption === currentItem.word ? 'Spot on context memory.' : `The correct answer was "${currentItem.word}".`}
                                </p>

                                <div className="space-y-3">
                                    <button
                                        onClick={handleNext}
                                        className="w-full py-3 bg-white text-black font-bold rounded-xl hover:bg-gray-200 transition-colors flex items-center justify-center gap-2"
                                    >
                                        Next Challenge <ChevronLeft className="w-4 h-4 rotate-180" />
                                    </button>

                                    {currentItem.videoUrl && (
                                        <a
                                            href={`${currentItem.videoUrl}&t=${Math.floor(currentItem.timestamp)}s`}
                                            target="_blank"
                                            className="block w-full py-3 bg-white/5 text-gray-300 font-medium rounded-xl hover:bg-white/10 transition-colors"
                                        >
                                            Watch Clip (Context)
                                        </a>
                                    )}
                                </div>
                            </div>
                        </div>
                    )}
                </div>
            </main>
        </div>
    );
}

function QuoteIcon({ className }: { className?: string }) {
    return (
        <svg className={className} xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="currentColor"><path d="M14.017 21L14.017 18C14.017 16.8954 14.9124 16 16.017 16H19.017C19.5693 16 20.017 15.5523 20.017 15V9C20.017 8.44772 19.5693 8 19.017 8H15.017C14.4647 8 14.017 8.44772 14.017 9V11C14.017 11.5523 13.5693 12 13.017 12H12.017V5H22.017V15C22.017 18.3137 19.3307 21 16.017 21H14.017ZM5.01691 21L5.01691 18C5.01691 16.8954 5.91234 16 7.01691 16H10.0169C10.5692 16 11.0169 15.5523 11.0169 15V9C11.0169 8.44772 10.5692 8 10.0169 8H6.01691C5.46462 8 5.01691 8.44772 5.01691 9V11C5.01691 11.5523 4.56919 12 4.01691 12H3.01691V5H13.0169V15C13.0169 18.3137 10.3306 21 7.01691 21H5.01691Z" /></svg>
    )
}
