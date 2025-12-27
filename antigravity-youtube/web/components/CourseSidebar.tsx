'use client';

import { useState, useEffect } from 'react';
import Link from 'next/link';
import { PlayCircle, CheckCircle, ChevronLeft, Circle } from 'lucide-react';

interface Lesson {
    id: string;
    title: string;
    duration: string;
    videoUrl?: string; // Optional
}

interface CourseSidebarProps {
    courseId: string;
    courseTitle: string;
    lessons: Lesson[];
    activeLessonId: string | null;
}

export default function CourseSidebar({ courseId, courseTitle, lessons, activeLessonId }: CourseSidebarProps) {
    const [completedLessonIds, setCompletedLessonIds] = useState<string[]>([]);

    // Load completed lessons from localStorage on mount
    useEffect(() => {
        const saved = localStorage.getItem(`course_progress_${courseId}`);
        if (saved) {
            try {
                setCompletedLessonIds(JSON.parse(saved));
            } catch (e) {
                console.error("Failed to parse course progress", e);
            }
        }
    }, [courseId]);

    // Save to localStorage whenever it changes
    const toggleLessonComplete = (lessonId: string, e: React.MouseEvent) => {
        e.preventDefault(); // Prevent navigation if clicking the icon
        e.stopPropagation();

        setCompletedLessonIds(prev => {
            let newIds;
            if (prev.includes(lessonId)) {
                newIds = prev.filter(id => id !== lessonId);
            } else {
                newIds = [...prev, lessonId];
            }
            localStorage.setItem(`course_progress_${courseId}`, JSON.stringify(newIds));
            return newIds;
        });
    };

    const progressPercentage = lessons.length > 0
        ? Math.round((completedLessonIds.length / lessons.length) * 100)
        : 0;

    return (
        <aside className="w-80 border-r border-gray-200 bg-[#F5F5F7] flex flex-col fixed top-0 bottom-0 left-0 pt-[48px] z-40 overflow-hidden">
            <div className="p-6 border-b border-gray-200/50 bg-[#F5F5F7]/95 backdrop-blur z-10">
                <Link href="/courses" className="text-sm text-[#86868b] hover:text-[#1d1d1f] flex items-center gap-1 mb-4 transition">
                    <ChevronLeft className="w-4 h-4" /> Back
                </Link>
                <h1 className="font-semibold text-[#1d1d1f] leading-tight line-clamp-2 mb-2">
                    {courseTitle}
                </h1>

                {/* Progress Bar */}
                <div className="flex items-center gap-2 mb-1">
                    <div className="flex-1 h-1.5 bg-gray-200 rounded-full overflow-hidden">
                        <div
                            className="h-full bg-green-500 rounded-full transition-all duration-500 ease-out"
                            style={{ width: `${progressPercentage}%` }}
                        />
                    </div>
                    <span className="text-xs font-medium text-[#86868b] w-8 text-right">{progressPercentage}%</span>
                </div>
                <p className="text-xs text-[#86868b]">{completedLessonIds.length} / {lessons.length} Completed</p>
            </div>

            <div className="flex-1 overflow-y-auto p-4 space-y-1">
                {lessons.map((lesson, index) => {
                    const isActive = lesson.id === activeLessonId;
                    const isCompleted = completedLessonIds.includes(lesson.id);

                    return (
                        <Link
                            key={lesson.id}
                            href={`/course/${courseId}?lesson=${lesson.id}`}
                            className={`group flex items-start gap-3 p-3 rounded-xl transition-all ${isActive ? 'bg-white shadow-sm ring-1 ring-black/5' : 'hover:bg-white/50'}`}
                        >
                            {/* Toggle Button */}
                            <button
                                onClick={(e) => toggleLessonComplete(lesson.id, e)}
                                className={`mt-0.5 w-5 h-5 rounded-full flex items-center justify-center shrink-0 transition-colors ${isCompleted
                                        ? 'text-green-500'
                                        : 'text-gray-300 hover:text-gray-400'
                                    }`}
                            >
                                {isCompleted ? (
                                    <CheckCircle className="w-5 h-5 fill-green-100" />
                                ) : (
                                    <Circle className="w-5 h-5" />
                                )}
                            </button>

                            <div className="flex-1 min-w-0">
                                <h3 className={`text-sm font-medium leading-snug ${isActive ? 'text-[#1d1d1f]' : 'text-[#424245]'}`}>
                                    {lesson.title}
                                </h3>
                                <div className="flex items-center gap-2 mt-1">
                                    {isActive && <PlayCircle className="w-3 h-3 text-blue-500" />}
                                    <p className="text-[11px] text-[#86868b]">{lesson.duration}</p>
                                </div>
                            </div>
                        </Link>
                    );
                })}
            </div>
        </aside>
    );
}
