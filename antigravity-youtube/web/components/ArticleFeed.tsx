'use client';

import { useState, useMemo } from 'react';
import { Article } from '@/lib/feishu';
import ArticleCard from './ArticleCard';
import MasonryGrid from './MasonryGrid';
import PodcastPlayer from './PodcastPlayer';
import { Search } from 'lucide-react';
import { getAllTags, mapTagToEnglish } from '@/lib/tags';

export default function ArticleFeed({ articles }: { articles: Article[] }) {
    const [searchQuery, setSearchQuery] = useState('');
    const [selectedTag, setSelectedTag] = useState('All');

    // Use the predefined English taxonomy
    const tags = getAllTags();

    // Filter logic with mapping
    const filteredArticles = useMemo(() => {
        return articles.filter(article => {
            const matchesSearch = (article.title + article.summary + article.goldenQuote).toLowerCase().includes(searchQuery.toLowerCase());

            // Map article tags to English for filtering
            const articleTagsEnglish = article.tags.map(mapTagToEnglish);

            const matchesTag = selectedTag === 'All' || articleTagsEnglish.includes(selectedTag);
            return matchesSearch && matchesTag;
        });
    }, [articles, searchQuery, selectedTag]);

    return (
        <div className="w-full max-w-[1600px] mx-auto px-6 lg:px-12">
            {/* Hero Search Section */}
            <div className="flex flex-col items-center justify-center py-24 text-center">
                <h1 className="text-[56px] leading-tight font-semibold text-[#1d1d1f] mb-6 tracking-tight">
                    降噪
                </h1>
                <p className="text-[21px] leading-relaxed text-[#86868b] font-medium mb-8 max-w-2xl">
                    MIKASA精选+AI生成，从海量信息中过滤噪音。<br />
                    5 分钟 获取全球优质深度洞察。
                </p>

                {/* Podcast Dual-Lang Player */}
                <div className="mb-10 w-full max-w-lg">
                    <PodcastPlayer />
                </div>

                <div className="relative w-full max-w-xl group">
                    <div className="absolute inset-y-0 left-5 flex items-center pointer-events-none">
                        <Search className="h-5 w-5 text-[#86868b]" />
                    </div>
                    <input
                        type="text"
                        className="w-full pl-14 pr-6 py-4 bg-white/80 backdrop-blur-xl border border-transparent group-hover:bg-white rounded-2xl shadow-[0_4px_16px_rgba(0,0,0,0.04)] focus:shadow-[0_8px_30px_rgba(0,0,0,0.12)] text-[17px] text-[#1d1d1f] focus:outline-none transition-all duration-300 placeholder:text-[#86868b]"
                        placeholder="Search insights..."
                        value={searchQuery}
                        onChange={(e) => setSearchQuery(e.target.value)}
                    />
                    <div className="absolute inset-y-0 right-5 flex items-center">
                        <kbd className="hidden sm:inline-flex items-center h-6 px-2 border border-[#d2d2d7] rounded-md text-[10px] font-medium text-[#86868b] bg-transparent">⌘K</kbd>
                    </div>
                </div>
            </div>

            {/* Sticky Tag Filter Row - Apple Style */}
            <div className="sticky top-[48px] z-40 py-4 mb-10 -mx-6 px-6 lg:-mx-12 lg:px-12 bg-[#F5F5F7]/80 backdrop-blur-xl border-b border-[#0000000a]">
                <div className="flex items-center justify-center gap-3 overflow-x-auto no-scrollbar pb-1 max-w-[1600px] mx-auto">
                    {tags.map((tag) => (
                        <button
                            key={tag}
                            onClick={() => setSelectedTag(tag)}
                            className={`px-4 py-1.5 rounded-full text-[13px] font-medium whitespace-nowrap transition-all duration-200 ease-out ${selectedTag === tag
                                ? 'bg-[#1d1d1f] text-white shadow-md transform scale-105'
                                : 'bg-white/50 text-[#1d1d1f]/70 hover:bg-white hover:text-[#1d1d1f] shadow-sm hover:shadow-md backdrop-blur-md'
                                }`}
                        >
                            {tag}
                        </button>
                    ))}
                </div>
            </div>

            {/* Results */}
            <div className="min-h-[400px]">
                {filteredArticles.length > 0 ? (
                    <MasonryGrid>
                        {filteredArticles.map((article) => (
                            <ArticleCard key={article.id} article={article} />
                        ))}
                    </MasonryGrid>
                ) : (
                    <div className="text-center py-32 text-[#86868b]">
                        <p className="text-lg font-medium">No results found.</p>
                    </div>
                )}
            </div>
        </div>
    );
}
