import { fetchCourses } from '@/lib/feishu';
import Link from 'next/link';
import { PlayCircle, Sparkles, BookOpen } from 'lucide-react';
import CourseGenerator from '@/components/CourseGenerator';

export const revalidate = 0; // Always fresh for now

function getGradient(seed: string) {
    const gradients = [
        'from-blue-400 to-indigo-600',
        'from-purple-400 to-pink-600',
        'from-green-400 to-emerald-600',
        'from-orange-400 to-red-600',
        'from-pink-400 to-rose-600',
        'from-indigo-400 to-cyan-600',
        'from-teal-400 to-green-600',
        'from-fuchsia-500 to-purple-600',
    ];
    let hash = 0;
    for (let i = 0; i < seed.length; i++) {
        hash = seed.charCodeAt(i) + ((hash << 5) - hash);
    }
    const index = Math.abs(hash) % gradients.length;
    return gradients[index];
}

export default async function CoursesPage() {
    const courses = await fetchCourses();

    return (
        <main className="min-h-screen bg-[#F5F5F7] text-[#1D1D1F] font-sans pb-20">
            {/* Header */}
            <div className="pt-32 pb-12 px-6 max-w-7xl mx-auto text-center">
                <h1 className="text-4xl md:text-5xl font-semibold tracking-tight mb-4 text-[#1D1D1F]">
                    Personal AI Tutor
                </h1>
                <p className="text-xl text-[#86868b] max-w-2xl mx-auto">
                    Tell us what you want to learn. We'll build a curriculum and find the best videos for you.
                </p>

                {/* Generator Input */}
                <div className="mt-10 max-w-2xl mx-auto relative group">
                    <CourseGenerator />
                </div>
            </div>

            {/* Course Grid */}
            <div className="max-w-7xl mx-auto px-6">
                <div className="flex items-center gap-2 mb-8">
                    <BookOpen className="w-5 h-5 text-[#86868b]" />
                    <h2 className="text-lg font-semibold text-[#86868b] uppercase tracking-wider">My Courses ({courses.length})</h2>
                </div>

                <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
                    {courses.map((course) => (
                        <Link href={`/course/${course.id}`} key={course.id} className="group block h-full">
                            <div className="bg-white rounded-[20px] overflow-hidden shadow-sm hover:shadow-2xl hover:-translate-y-1 transition-all duration-300 border border-gray-100 h-full flex flex-col relative">
                                {/* Cover Image / Gradient */}
                                <div className="aspect-[16/9] bg-gray-100 relative overflow-hidden">
                                    {course.cover ? (
                                        <>
                                            <img
                                                src={course.cover}
                                                alt={course.title}
                                                className="w-full h-full object-cover group-hover:scale-105 transition duration-700 ease-out"
                                            />
                                            {/* Gradient Overlay for text readability if we needed it, but we put text below */}
                                        </>
                                    ) : (
                                        <div className={`w-full h-full flex items-center justify-center p-6 bg-gradient-to-br ${getGradient(course.title)}`}>
                                            <span className="text-white/40 font-bold text-4xl select-none opacity-50 mix-blend-overlay">
                                                {course.title.charAt(0)}
                                            </span>
                                        </div>
                                    )}

                                    {/* Glassmorphism Play Button Overlay */}
                                    <div className="absolute inset-0 bg-black/10 group-hover:bg-black/20 transition-colors flex items-center justify-center opacity-0 group-hover:opacity-100 duration-300 backdrop-blur-[2px]">
                                        <div className="bg-white/30 backdrop-blur-md text-white rounded-full p-3 shadow-lg transform scale-90 group-hover:scale-110 transition-all duration-300 border border-white/50">
                                            <PlayCircle className="w-8 h-8 fill-current" />
                                        </div>
                                    </div>

                                    {/* Status Badge - Absolute Positioned */}
                                    <div className="absolute top-3 right-3">
                                        <span className={`px-2.5 py-1 text-[10px] font-bold uppercase tracking-wide rounded-full backdrop-blur-md shadow-sm border border-white/20 ${course.status === 'Done'
                                            ? 'bg-green-500/90 text-white'
                                            : 'bg-yellow-500/90 text-white animate-pulse'
                                            }`}>
                                            {course.status === 'Done' ? 'Ready' : 'Building'}
                                        </span>
                                    </div>
                                </div>

                                <div className="p-5 flex-1 flex flex-col">
                                    <h3 className="text-lg font-bold text-gray-900 mb-2 line-clamp-2 leading-tight group-hover:text-blue-600 transition-colors">
                                        {course.title}
                                    </h3>
                                    <p className="text-gray-500 text-xs leading-relaxed line-clamp-3 mb-4 flex-1">
                                        {course.description || "An AI-curated course tailored just for you."}
                                    </p>

                                    <div className="flex items-center justify-between text-[10px] font-medium text-gray-400 pt-3 border-t border-gray-50">
                                        <span className="flex items-center gap-1">
                                            <Sparkles className="w-3 h-3 text-purple-400" />
                                            AI Generated
                                        </span>
                                        <span>Course</span>
                                    </div>
                                </div>
                            </div>
                        </Link>
                    ))}
                </div>
            </div>
        </main>
    );
}
