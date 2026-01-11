'use client';

import { useState } from 'react';
import { Sparkles, Loader2 } from 'lucide-react';
import { useRouter } from 'next/navigation';

export default function CourseGenerator() {
    const [topic, setTopic] = useState('');
    const [isLoading, setIsLoading] = useState(false);
    const router = useRouter();

    const handleGenerate = async () => {
        if (!topic.trim()) return;

        setIsLoading(true);
        try {
            const res = await fetch('/api/course/generate', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ topic }),
            });

            if (res.ok) {
                setTopic('');
                router.refresh(); // Refresh Server Components to show new course
            } else {
                alert('Generation failed. Check console.');
            }
        } catch (e) {
            console.error(e);
            alert('Error generating course');
        } finally {
            setIsLoading(false);
        }
    };

    return (
        <div className="mt-10 max-w-2xl mx-auto relative group">
            <div className="absolute inset-0 bg-gradient-to-r from-blue-500 to-purple-500 rounded-full blur opacity-20 group-hover:opacity-30 transition duration-500"></div>
            <div className="relative flex items-center bg-white/80 backdrop-blur-xl rounded-full border border-white/40 shadow-lg p-2">
                <div className="pl-4 text-purple-500">
                    <Sparkles className="w-6 h-6" />
                </div>
                <input
                    type="text"
                    value={topic}
                    onChange={(e) => setTopic(e.target.value)}
                    onKeyDown={(e) => e.key === 'Enter' && handleGenerate()}
                    disabled={isLoading}
                    placeholder="I want to learn..."
                    className="flex-1 bg-transparent border-none outline-none px-4 text-lg text-[#1D1D1F] placeholder:text-[#86868b]/70 h-12 disabled:opacity-50"
                />
                <button
                    onClick={handleGenerate}
                    disabled={isLoading || !topic.trim()}
                    className="bg-[#1D1D1F] text-white px-8 h-12 rounded-full font-medium hover:bg-black transition-all flex items-center gap-2 disabled:bg-gray-400"
                >
                    {isLoading ? (
                        <>
                            <Loader2 className="w-4 h-4 animate-spin" />
                            Building...
                        </>
                    ) : (
                        'Generate'
                    )}
                </button>
            </div>
            {isLoading && (
                <p className="text-center text-xs text-purple-600 mt-2 animate-pulse">
                    AI is designing your curriculum... (This takes ~1 minute)
                </p>
            )}
        </div>
    );
}
