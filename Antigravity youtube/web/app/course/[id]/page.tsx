import { fetchCourses, fetchLessons } from '@/lib/feishu';
import Link from 'next/link';
import { PlayCircle, CheckCircle, ChevronLeft, Menu } from 'lucide-react';
import { redirect } from 'next/navigation';
import CourseQuiz from '@/components/CourseQuiz';
import CourseNotes from '@/components/CourseNotes';
import CourseSidebar from '@/components/CourseSidebar';

export const revalidate = 0;

interface PageProps {
    params: Promise<{ id: string }>;
    searchParams: Promise<{ lesson?: string }>;
}

function getYouTubeId(url: string) {
    const regExp = /^.*(youtu.be\/|v\/|u\/\w\/|embed\/|watch\?v=|&v=)([^#&?]*).*/;
    const match = url?.match(regExp);
    return (match && match[2].length === 11) ? match[2] : null;
}

export default async function CoursePlayerPage(props: PageProps) {
    const params = await props.params;
    const searchParams = await props.searchParams;
    const courseId = params.id;

    // Fetch Data
    const [courses, lessons] = await Promise.all([
        fetchCourses(),
        fetchLessons(courseId)
    ]);

    const course = courses.find(c => c.id === courseId);

    if (!course) {
        return (
            <div className="min-h-screen flex items-center justify-center bg-[#F5F5F7]">
                <div className="text-center">
                    <h1 className="text-2xl font-semibold mb-2">Course Not Found</h1>
                    <Link href="/courses" className="text-blue-500 hover:underline">Back to Courses</Link>
                </div>
            </div>
        );
    }

    // Sort lessons if needed (Feishu returns insertion order usually, which matches our generation)
    // If we had a sort order field, we'd sort here.

    const activeLessonId = searchParams.lesson || (lessons.length > 0 ? lessons[0].id : null);
    const activeLesson = lessons.find(l => l.id === activeLessonId);

    return (
        <div className="min-h-screen bg-white flex">
            {/* Sidebar */}
            <CourseSidebar
                courseId={courseId}
                courseTitle={course.title}
                lessons={lessons}
                activeLessonId={activeLessonId}
            />

            {/* Main Content */}
            <main className="flex-1 ml-80 pt-[48px] min-h-screen flex flex-col">
                {activeLesson ? (
                    <div className="flex-1 max-w-5xl mx-auto w-full p-8 lg:p-12">
                        <div className="aspect-video bg-black rounded-[24px] overflow-hidden shadow-2xl mb-8 relative group">
                            {activeLesson.videoUrl ? (
                                <iframe
                                    src={`https://www.youtube.com/embed/${getYouTubeId(activeLesson.videoUrl)}?autoplay=1&rel=0`}
                                    className="w-full h-full"
                                    title={activeLesson.title}
                                    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                                    allowFullScreen
                                />
                            ) : (
                                <div className="w-full h-full flex items-center justify-center text-gray-500">
                                    Video URL missing
                                </div>
                            )}
                        </div>

                        <div className="max-w-3xl">
                            <div className="flex items-center gap-3 text-sm font-medium text-blue-600 mb-2">
                                <span>{activeLesson.moduleTitle}</span>
                            </div>
                            <h2 className="text-3xl font-semibold text-[#1d1d1f] mb-4">
                                {activeLesson.title}
                            </h2>
                            {/* Placeholder for future Lesson Notes / AI Summary */}
                            <div className="prose prose-gray mb-8">
                                <p className="text-[#86868b]">
                                    Watch this lesson to master the concepts of {activeLesson.title}.
                                </p>
                            </div>

                            <CourseQuiz
                                courseTitle={course.title}
                                lessonTitle={activeLesson.title}
                            />

                            <CourseNotes
                                courseTitle={course.title}
                                lessonTitle={activeLesson.title}
                                lessonId={activeLesson.id}
                            />
                        </div>
                    </div>
                ) : (
                    <div className="flex-1 flex items-center justify-center text-[#86868b]">
                        No lessons available for this course.
                    </div>
                )}
            </main>
        </div>
    );
}
