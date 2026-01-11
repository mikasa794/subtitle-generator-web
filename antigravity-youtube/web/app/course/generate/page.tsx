import CourseGenerator from '@/components/CourseGenerator';

export default function GenerateCoursePage() {
    return (
        <div className="min-h-screen bg-[#F5F5F7] flex flex-col items-center justify-center p-4">
            <div className="text-center mb-10">
                <h1 className="text-4xl font-semibold tracking-tight text-gray-900 mb-4">
                    Personalized AI Course
                </h1>
                <p className="text-lg text-gray-500 max-w-lg mx-auto">
                    Whatever you want to learn, we'll design a perfect curriculum and curate the best videos for you.
                </p>
            </div>

            <div className="w-full">
                <CourseGenerator />
            </div>

            <div className="mt-20 text-sm text-gray-400">
                Powered by Antigravity AI
            </div>
        </div>
    );
}
