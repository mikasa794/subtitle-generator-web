'use client';

import { Article } from '@/lib/feishu';
import { Heart, ExternalLink, Play } from 'lucide-react';
import { useState, useEffect } from 'react';
import Link from 'next/link';
import { mapTagToEnglish } from '@/lib/tags';

// Simplified fallback image generator if none provided
const getFallbackImage = (id: string) => `https://picsum.photos/seed/${id}/800/450`;

export default function ArticleCard({ article }: { article: Article }) {
    const [isLiked, setIsLiked] = useState(false);

    // Load favorite state on mount
    useEffect(() => {
        const favorites = JSON.parse(localStorage.getItem('denoise_favorites') || '[]');
        if (favorites.includes(article.id)) {
            setIsLiked(true);
        }
    }, [article.id]);

    const toggleLike = (e: React.MouseEvent) => {
        e.preventDefault();
        e.stopPropagation();

        const favorites = JSON.parse(localStorage.getItem('denoise_favorites') || '[]');
        let newFavorites;

        if (isLiked) {
            newFavorites = favorites.filter((id: string) => id !== article.id);
        } else {
            newFavorites = [...favorites, article.id];
        }

        localStorage.setItem('denoise_favorites', JSON.stringify(newFavorites));
        setIsLiked(!isLiked);
    };

    return (
        <Link href={`/article/${article.id}`} className="block group relative bg-white rounded-[22px] overflow-hidden shadow-[0_2px_8px_rgba(0,0,0,0.04)] hover:shadow-[0_12px_24px_rgba(0,0,0,0.08)] transition-all duration-500 transform hover:-translate-y-1 mb-6 break-inside-avoid ring-1 ring-black/5">
            {/* Cover Image */}
            <div className="relative aspect-video overflow-hidden bg-gray-50">
                <img
                    src={article.cover ? `/api/image-proxy?url=${encodeURIComponent(article.cover)}` : getFallbackImage(article.id)}
                    alt={article.title}
                    className="object-cover w-full h-full group-hover:scale-105 transition-transform duration-700 ease-out"
                    loading="lazy"
                />
                <div className="absolute inset-0 bg-black/5 opacity-0 group-hover:opacity-100 transition-opacity duration-500" />

                {/* Top Right Actions: Like Button */}
                <div className="absolute top-3 right-3 flex gap-2 opacity-0 group-hover:opacity-100 transition-opacity duration-300 translate-y-2 group-hover:translate-y-0 z-10">
                    <button
                        onClick={toggleLike}
                        className={`p-2.5 rounded-full backdrop-blur-xl transition-all duration-300 ${isLiked ? 'bg-red-500/90 text-white shadow-lg' : 'bg-white/80 text-gray-700 hover:bg-white shadow-sm'}`}
                    >
                        <Heart size={18} fill={isLiked ? "currentColor" : "none"} />
                    </button>
                </div>

                {/* Bottom Right Actions: YouTube Button (New Request) */}
                <div className="absolute bottom-3 right-3 opacity-0 group-hover:opacity-100 transition-opacity duration-300 translate-y-2 group-hover:translate-y-0 z-10">
                    <a
                        href={article.url}
                        target="_blank"
                        rel="noreferrer"
                        onClick={(e) => e.stopPropagation()}
                        className="flex items-center gap-1.5 px-3 py-1.5 bg-black/70 hover:bg-[#FF0000]/90 backdrop-blur-md text-white rounded-full transition-colors shadow-lg group/btn"
                    >
                        <span className="text-[11px] font-medium tracking-wide">YouTube</span>
                        <ExternalLink size={12} className="group-hover/btn:translate-x-0.5 transition-transform" />
                    </a>
                </div>
            </div>

            <div className="p-6">
                {/* Meta Header - Apple Style Tags */}
                <div className="flex flex-wrap items-center gap-2 mb-4">
                    {article.tags.slice(0, 3).map(mapTagToEnglish).map((tag, index) => (
                        <span key={index} className="px-3 py-1 rounded-full bg-gray-100/80 text-[#1d1d1f] text-[11px] font-medium tracking-wide">
                            {tag}
                        </span>
                    ))}
                    <span className="text-[#86868b] text-[11px] font-medium ml-auto tracking-wide uppercase">{article.date}</span>
                </div>

                {/* Title */}
                <h3 className="text-[19px] font-semibold text-[#1d1d1f] mb-3 leading-snug group-hover:text-[#06c] transition-colors line-clamp-2 tracking-tight">
                    {article.title}
                </h3>

                {/* Author Footer */}
                <div className="flex items-center justify-between pt-4 mt-2">
                    <div className="flex items-center gap-2">
                        <div className="w-6 h-6 rounded-full bg-gray-100 flex items-center justify-center text-[10px] font-bold text-gray-500">
                            {article.author.slice(0, 1)}
                        </div>
                        <span className="text-xs text-[#86868b] font-medium truncate max-w-[120px]">{article.author}</span>
                    </div>

                    {/* Old footer icon removed in favor of the prominent image overlay */}
                </div>
            </div>
        </Link>
    );
}
