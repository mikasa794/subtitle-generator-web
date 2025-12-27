'use client';

import { useEffect, useState } from 'react';
import { Article } from '@/lib/feishu';
import ArticleCard from './ArticleCard';
import MasonryGrid from './MasonryGrid';
import Link from 'next/link';
import { ArrowLeft, Bookmark } from 'lucide-react';

export default function FavoritesList({ articles }: { articles: Article[] }) {
    const [favoriteIds, setFavoriteIds] = useState<string[]>([]);
    const [mounted, setMounted] = useState(false);

    useEffect(() => {
        const stored = JSON.parse(localStorage.getItem('denoise_favorites') || '[]');
        setFavoriteIds(stored);
        setMounted(true);
    }, []);

    const favoriteArticles = articles.filter(a => favoriteIds.includes(a.id));

    if (!mounted) return null; // Avoid hydration mismatch

    return (
        <div className="container mx-auto px-6 py-8">
            <div className="flex items-center gap-4 mb-8">
                <Link href="/" className="p-2 hover:bg-gray-200 rounded-full transition-colors">
                    <ArrowLeft className="text-gray-600" />
                </Link>
                <h1 className="text-3xl font-black text-gray-900">我的收藏</h1>
                <span className="bg-blue-100 text-blue-700 font-bold px-3 py-1 rounded-full text-sm">
                    {favoriteArticles.length}
                </span>
            </div>

            {favoriteArticles.length > 0 ? (
                <MasonryGrid>
                    {favoriteArticles.map(article => (
                        <ArticleCard key={article.id} article={article} />
                    ))}
                </MasonryGrid>
            ) : (
                <div className="flex flex-col items-center justify-center py-20 text-gray-400">
                    <Bookmark size={64} strokeWidth={1} className="mb-4 text-gray-300" />
                    <p className="text-xl font-medium">还没有收藏任何内容</p>
                    <Link href="/" className="mt-4 text-blue-600 hover:underline">
                        去首页逛逛
                    </Link>
                </div>
            )}
        </div>
    );
}
