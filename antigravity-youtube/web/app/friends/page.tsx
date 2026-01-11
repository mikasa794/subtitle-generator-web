'use client';

import Link from 'next/link';

export default function FriendsLanding() {
    return (
        <div className="min-h-screen bg-[#7B538C] flex flex-col items-center justify-center p-6 text-white font-sans relative overflow-hidden">
            {/* Background Decor */}
            <div className="absolute top-0 left-0 w-full h-full pointer-events-none opacity-20">
                <div className="absolute top-10 left-10 w-20 h-20 border-4 border-[#F2C94C] rounded-full"></div>
                <div className="absolute bottom-20 right-20 w-32 h-32 border-8 border-[#F2C94C] transform rotate-12"></div>
            </div>

            {/* Main Card */}
            <div className="bg-[#1e1e1e] border-4 border-[#F2C94C] p-8 md:p-12 rounded-3xl max-w-md w-full shadow-2xl relative z-10 text-center">
                {/* Frame Icon */}
                <div className="w-16 h-20 border-4 border-[#F2C94C] mx-auto mb-6 rounded-lg bg-[#7B538C] shadow-inner flex items-center justify-center">
                    <div className="w-2 h-2 bg-black rounded-full"></div>
                </div>

                <h1 className="text-4xl md:text-5xl font-extrabold mb-2 tracking-tighter text-white drop-shadow-md">
                    The One With<br />The Quiz
                </h1>
                <p className="text-[#F2C94C] text-lg font-medium mb-8">
                    Are you a Joey, a Mon, or a Chanandler Bong?
                </p>

                <Link
                    href="/friends/play"
                    className="block w-full py-4 bg-[#F2C94C] hover:bg-[#d9b442] text-black font-black text-xl uppercase tracking-widest rounded-xl transition-transform hover:scale-105 shadow-lg mb-4"
                >
                    Start Video Challenge
                </Link>

                <Link
                    href="/friends/written"
                    className="block w-full py-4 bg-transparent border-2 border-[#F2C94C] text-[#F2C94C] hover:bg-[#F2C94C]/10 font-bold text-lg uppercase tracking-widest rounded-xl transition-all"
                >
                    The Written Exam 📝
                </Link>

                <p className="mt-6 text-gray-500 text-xs">
                    *We don't know who you are, but we'll find out.
                </p>
            </div>
        </div>
    );
}
