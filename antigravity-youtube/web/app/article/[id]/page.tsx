import { fetchArticleById } from '@/lib/feishu';
import { notFound } from 'next/navigation';
import Link from 'next/link';
import { ArrowLeft, ExternalLink, Calendar, User } from 'lucide-react';
import ReactMarkdown from 'react-markdown';
import { mapTagToEnglish } from '@/lib/tags';

export default async function ArticleDetail(props: { params: Promise<{ id: string }> }) {
    const params = await props.params;
    const article = await fetchArticleById(params.id);

    if (!article) {
        notFound();
    }

    // Use proxy for images
    const coverImage = article.cover
        ? `/api/image-proxy?url=${encodeURIComponent(article.cover)}`
        : `https://picsum.photos/seed/${article.id}/1920/1080`;

    return (
        <main className="min-h-screen bg-white">
            {/* Immersive Hero Header */}
            <div className="relative h-[65vh] w-full overflow-hidden">
                {/* Background Image with Blur */}
                <div
                    className="absolute inset-0 bg-cover bg-center scale-105"
                    style={{ backgroundImage: `url(${coverImage})` }}
                >
                    <div className="absolute inset-0 bg-black/40 backdrop-blur-md" />
                    <div className="absolute inset-0 bg-gradient-to-t from-black/80 via-black/20 to-transparent" />
                </div>

                {/* Hero Content */}
                <div className="relative h-full container mx-auto px-6 lg:px-12 flex flex-col justify-end pb-24 text-white z-10 max-w-6xl">
                    <Link href="/" className="absolute top-12 left-6 lg:left-12 inline-flex items-center text-white/70 hover:text-white transition-colors bg-black/20 backdrop-blur-xl px-4 py-2 rounded-full text-sm font-medium">
                        <ArrowLeft size={16} className="mr-2" />
                        Back
                    </Link>

                    <div className="flex flex-wrap gap-2 mb-8">
                        {article.tags.map((tag) => (
                            <span key={tag} className="px-3.5 py-1.5 rounded-full bg-white/10 backdrop-blur-md border border-white/20 text-sm font-medium tracking-wide">
                                {mapTagToEnglish(tag)}
                            </span>
                        ))}
                    </div>

                    <h1 className="text-5xl lg:text-7xl font-semibold leading-tight mb-8 tracking-tight text-white/95">
                        {article.title}
                    </h1>

                    <div className="flex items-center gap-8 text-white/80 font-medium text-lg">
                        <div className="flex items-center gap-2.5">
                            <User size={20} />
                            <span>{article.author}</span>
                        </div>
                        <div className="flex items-center gap-2.5">
                            <Calendar size={20} />
                            <span>{article.date}</span>
                        </div>
                        <a
                            href={article.url}
                            target="_blank"
                            rel="noreferrer"
                            className="flex items-center gap-2 px-6 py-2.5 rounded-full bg-white text-black hover:bg-white/90 transition-all font-semibold ml-auto"
                        >
                            <ExternalLink size={18} />
                            <span>Watch Original</span>
                        </a>
                    </div>
                </div>
            </div>

            {/* Main Content Layout */}
            <div className="container mx-auto px-6 lg:px-12 py-20 max-w-6xl">
                <div className="grid grid-cols-1 lg:grid-cols-12 gap-16">

                    {/* Sticky Sidebar (Left) */}
                    <div className="lg:col-span-3 hidden lg:block">
                        <div className="sticky top-32">
                            <h3 className="text-xs font-semibold text-[#86868b] uppercase tracking-wider mb-6">
                                Contents
                            </h3>
                            <nav className="flex flex-col space-y-4">
                                <a href="#summary" className="text-[#1d1d1f] font-medium hover:text-[#06c] transition-colors relative pl-4 border-l-2 border-[#1d1d1f]">
                                    In Depth
                                </a>
                                <a href="#quote" className="text-[#86868b] font-medium hover:text-[#1d1d1f] transition-colors pl-4 border-l-2 border-transparent">
                                    Highlights
                                </a>
                            </nav>
                        </div>
                    </div>

                    {/* Content Area (Right) */}
                    <div className="lg:col-span-8 space-y-16">

                        {/* Creation Note / Summary */}
                        <section id="summary">
                            <div className="prose prose-lg prose-gray max-w-none text-[#1d1d1f] leading-loose">
                                <ReactMarkdown
                                    components={{
                                        h1: ({ node, ...props }) => <h1 className="text-3xl font-semibold text-[#1d1d1f] mt-16 mb-8 tracking-tight" {...props} />,
                                        h2: ({ node, ...props }) => <h2 className="text-2xl font-semibold text-[#1d1d1f] mt-16 mb-6 tracking-tight relative" {...props} />,
                                        h3: ({ node, ...props }) => <h3 className="text-xl font-semibold text-[#1d1d1f] mt-10 mb-4 tracking-tight" {...props} />,
                                        p: ({ node, ...props }) => <p className="mb-6 text-[18px] text-[#1d1d1f]/80 leading-relaxed font-normal" {...props} />,
                                        strong: ({ node, ...props }) => <strong className="font-semibold text-[#1d1d1f]" {...props} />,
                                        blockquote: ({ node, ...props }) => <blockquote className="border-l-[3px] border-[#1d1d1f] pl-6 italic text-[#1d1d1f] my-10 font-medium text-xl" {...props} />,
                                        ul: ({ node, ...props }) => <ul className="list-disc pl-6 my-6 space-y-3 text-[#1d1d1f]/80" {...props} />,
                                        ol: ({ node, ...props }) => <ol className="list-decimal pl-6 my-6 space-y-3 text-[#1d1d1f]/80" {...props} />,
                                    }}
                                >
                                    {article.summary}
                                </ReactMarkdown>
                            </div>
                        </section>

                        {/* Golden Quotes Section */}
                        {article.goldenQuote && (
                            <section id="quote" className="py-12 border-t border-[#f5f5f7]">
                                <h2 className="text-xs font-semibold text-[#86868b] uppercase tracking-wider mb-8">
                                    Quote of the day
                                </h2>
                                <blockquote className="space-y-6">
                                    {article.goldenQuote.split('\n').map((line, i) => (
                                        line.trim() && (
                                            <p key={i} className="text-2xl md:text-3xl font-semibold text-[#1d1d1f] leading-tight tracking-tight">
                                                "{line}"
                                            </p>
                                        )
                                    ))}
                                </blockquote>
                            </section>
                        )}

                    </div>
                </div>
            </div>
        </main>
    );
}
