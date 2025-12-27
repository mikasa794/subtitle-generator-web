'use client';

import { useState, useRef, useEffect } from 'react';
import { Play, Pause, Download, Globe } from 'lucide-react';

export default function PodcastPlayer() {
    const [lang, setLang] = useState<'en' | 'cn'>('cn'); // Default to CN based on user preference
    const [isPlaying, setIsPlaying] = useState(false);

    const audioRef = useRef<HTMLAudioElement>(null);

    // Reset audio when language changes
    useEffect(() => {
        if (audioRef.current) {
            audioRef.current.load();
            if (isPlaying) {
                audioRef.current.play().catch(e => console.error("Play error:", e));
            }
        }
    }, [lang]);

    const togglePlay = () => {
        if (!audioRef.current) return;
        if (isPlaying) {
            audioRef.current.pause();
        } else {
            audioRef.current.play();
        }
        setIsPlaying(!isPlaying);
    };

    const handleEnded = () => setIsPlaying(false);

    const currentSrc = lang === 'en' ? '/podcast_demo_en.mp3' : '/podcast_demo_cn.mp3';
    const currentTitle = lang === 'en' ? 'Morning Briefing (AI Generated)' : '早安播报 (AI生成)';
    const hosts = lang === 'en' ? 'Alex & Jamie' : '云希 & 晓晓';

    return (
        <div className="w-full max-w-lg mb-12 p-1 bg-white/60 backdrop-blur-xl rounded-[28px] shadow-[0_8px_32px_rgba(0,0,0,0.06)] border border-white/20">
            <audio
                ref={audioRef}
                src={currentSrc}
                onEnded={handleEnded}
                onPause={() => setIsPlaying(false)}
                onPlay={() => setIsPlaying(true)}
            />

            <div className="flex items-center p-3 gap-4">
                {/* Play Button */}
                <button
                    onClick={togglePlay}
                    className="flex-shrink-0 w-12 h-12 flex items-center justify-center rounded-full bg-[#1d1d1f] text-white hover:scale-105 transition-transform shadow-lg"
                >
                    {isPlaying ? <Pause size={20} fill="currentColor" /> : <Play size={20} fill="currentColor" className="ml-0.5" />}
                </button>

                {/* Info Text */}
                <div className="flex-grow min-w-0">
                    <h3 className="text-[15px] font-semibold text-[#1d1d1f] truncate">{currentTitle}</h3>
                    <p className="text-[12px] text-[#86868b] font-medium flex items-center gap-1.5">
                        <span>🎙️ {hosts}</span>
                    </p>
                </div>

                {/* Controls Right */}
                <div className="flex items-center gap-2">
                    {/* Language Toggle */}
                    <div className="flex bg-[#e5e5ea]/50 p-1 rounded-full relative">
                        <div
                            className={`absolute inset-y-1 w-[32px] bg-white rounded-full shadow-sm transition-all duration-300 ease-spring ${lang === 'en' ? 'left-1' : 'left-[38px]'}`}
                        />
                        <button
                            onClick={() => setLang('en')}
                            className={`relative z-10 w-[32px] h-[24px] text-[10px] font-bold rounded-full transition-colors ${lang === 'en' ? 'text-black' : 'text-gray-400'}`}
                        >
                            EN
                        </button>
                        <button
                            onClick={() => setLang('cn')}
                            className={`relative z-10 w-[32px] h-[24px] text-[10px] font-bold rounded-full transition-colors ${lang === 'cn' ? 'text-black' : 'text-gray-400'}`}
                        >
                            CN
                        </button>
                    </div>

                    {/* Download */}
                    <a
                        href={currentSrc}
                        download
                        className="p-2 text-[#86868b] hover:text-[#1d1d1f] transition-colors"
                        title="Download MP3"
                    >
                        <Download size={18} />
                    </a>
                </div>
            </div>
        </div>
    );
}
