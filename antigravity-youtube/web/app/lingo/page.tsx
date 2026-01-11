import Link from 'next/link';
import { fetchLingoClips } from '@/lib/feishu';
import { PlayCircle, Globe, BookOpen } from 'lucide-react';

// Disable caching to see new clips instantly
export const revalidate = 0;

export default async function LingoPage() {
    // Fetch clips (no filter, get all)
    const clips = await fetchLingoClips();

    return (
        <div className="min-h-screen bg-[#F5F5F7] p-8 font-sans">
            <header className="max-w-7xl mx-auto mb-12 flex items-center justify-between">
                <div>
                    <h1 className="text-4xl font-bold text-[#1d1d1f] tracking-tight mb-2">
                        LingoTube
                    </h1>
                    <p className="text-xl text-[#86868b]">
                        Immersive Language Learning with TV & Anime.
                    </p>
                </div>
                <Link href="/import" className="text-sm font-semibold text-teal-600 hover:text-teal-500 bg-teal-50 px-4 py-2 rounded-full border border-teal-100 transition-colors">
                    + Creator Center
                </Link>
            </header>

            <main className="max-w-7xl mx-auto">
                {clips.length === 0 ? (
                    <div className="text-center py-20">
                        <p className="text-gray-500 text-lg">No clips found yet. Generate some!</p>
                    </div>
                ) : (
                    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                        {clips.map((clip) => (
                            <Link href={`/lingo/${clip.id}`} key={clip.id} className="group block">
                                <div className="bg-white rounded-[20px] overflow-hidden shadow-sm hover:shadow-xl transition-all duration-300 border border-gray-100 h-full flex flex-col">
                                    {/* Thumbnail Placeholder or Actual if we had it */}
                                    <div className="aspect-video bg-gray-100 relative overflow-hidden">
                                        {/* Cover Image or Gradient Fallback */}
                                        {clip.cover ? (
                                            <img
                                                src={clip.cover}
                                                alt={clip.title}
                                                className="absolute inset-0 w-full h-full object-cover transition-transform duration-500 group-hover:scale-105"
                                            />
                                        ) : (
                                            <div className={`absolute inset-0 ${clip.series.includes('Friends') ? 'bg-gradient-to-br from-orange-100 to-yellow-100' :
                                                clip.series.includes('Conan') ? 'bg-gradient-to-br from-blue-100 to-cyan-100' :
                                                    'bg-gradient-to-br from-purple-100 to-pink-100'
                                                }`} />
                                        )}

                                        <div className="absolute inset-0 flex items-center justify-center bg-black/0 group-hover:bg-black/10 transition-colors z-10">
                                            <PlayCircle className="w-12 h-12 text-white opacity-90 shadow-lg rounded-full bg-black/20 backdrop-blur-sm group-hover:scale-110 transition-transform" />
                                        </div>

                                        <div className="absolute top-3 right-3 bg-black/60 backdrop-blur-md text-white px-3 py-1 rounded-full text-xs font-medium flex items-center gap-1">
                                            <Globe className="w-3 h-3" />
                                            {clip.targetLang}
                                        </div>
                                    </div>

                                    <div className="p-6 flex-1 flex flex-col">
                                        <div className="flex items-center gap-2 text-xs font-semibold text-blue-600 mb-2 uppercase tracking-wider">
                                            <BookOpen className="w-3 h-3" />
                                            {clip.series}
                                        </div>
                                        <h3 className="text-xl font-bold text-[#1d1d1f] mb-2 line-clamp-2 group-hover:text-blue-600 transition-colors">
                                            {clip.title}
                                        </h3>
                                        <div className="mt-auto pt-4 flex items-center justify-between text-xs text-gray-400">
                                            <span className="bg-gray-100 px-2 py-1 rounded-md">{clip.difficulty}</span>
                                            <span>Start Learning →</span>
                                        </div>
                                    </div>
                                </div>
                            </Link>
                        ))}
                    </div>
                )}
            </main>
        </div>
    );
}
