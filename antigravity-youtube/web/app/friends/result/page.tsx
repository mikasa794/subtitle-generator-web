'use client';

import { Suspense, useState } from 'react';
import { useSearchParams } from 'next/navigation';
import Link from 'next/link';

function ResultContent() {
    const searchParams = useSearchParams();

    // Parse scores
    const scores: Record<string, number> = {};
    let maxScore = -1;
    let mainPersona = "Joey"; // Default

    const PERSONAS = ['Joey', 'Monica', 'Ross', 'Chandler', 'Rachel', 'Phoebe'];
    let totalPoints = 0;

    let topCandidates: string[] = [];

    // First pass: Calculate and find max
    PERSONAS.forEach(p => {
        const s = parseInt(searchParams.get(p) || '0');
        scores[p] = s;
        totalPoints += s;
        if (s > maxScore) {
            maxScore = s;
            topCandidates = [p];
        } else if (s === maxScore) {
            topCandidates.push(p);
        }
    });

    // Tie-breaker: Randomly pick one of the top candidates to avoid "Joey bias"
    if (topCandidates.length > 0) {
        // Use a simple hash of the params string to be consistent on refresh? 
        // Or pure random? Pure random is arguably more fun "try again to maybe see another side".
        // Let's stick to consistent for now so refreshing doesn't confuse them, BUT 
        // the user *complained* about the bias. 
        // Actually, let's use the sum of char codes of the query string as a seed sort of?
        // No, let's just do random.
        mainPersona = topCandidates[Math.floor(Math.random() * topCandidates.length)];
    }

    if (totalPoints === 0) totalPoints = 1;

    // Descriptions
    const DESCRIPTIONS: Record<string, string> = {
        Joey: "You prioritize food over everything. You're loyal, simple, and 'How you doin'?' is your answer to life.",
        Monica: "You are the glue. You need rules, you need order, and you probably organized this quiz for us.",
        Ross: "You are fine. You are totally fine. (You are not fine). PIVOT!",
        Chandler: "You make jokes when you are uncomfortable. Which is always.",
        Rachel: "You are finding your footing. And you probably exchanged those gifts.",
        Phoebe: "You are wonderfully weird. Smelly Cat is your anthem."
    };

    return (
        <div className="bg-[#1e1e1e] border-4 border-[#F2C94C] p-8 rounded-3xl max-w-md w-full shadow-2xl relative z-10 text-center animate-in zoom-in-95 duration-500 overflow-hidden">
            {/* Frame Icon */}
            <div className="w-24 h-28 border-4 border-[#F2C94C] mx-auto mb-6 rounded-lg bg-[#7B538C] shadow-inner flex items-center justify-center">
                <span className="text-4xl">🍕</span>
            </div>

            <h2 className="text-gray-400 font-bold uppercase tracking-widest text-sm mb-2">The Results Are In</h2>
            <h1 className="text-5xl font-extrabold text-white mb-6">
                You are<br />
                <span className="text-[#F2C94C]">{mainPersona}</span>
            </h1>

            <p className="text-gray-300 text-lg mb-8 leading-relaxed italic">
                "{DESCRIPTIONS[mainPersona]}"
            </p>

            {/* Breakdown */}
            <div className="bg-black/20 p-4 rounded-xl text-left space-y-3 mb-8">
                <h3 className="text-white/50 font-bold text-xs uppercase tracking-wider mb-4 border-b border-white/10 pb-2">Personality Mix</h3>
                {PERSONAS.map(p => {
                    const pct = Math.round((scores[p] / totalPoints) * 100);
                    const isMain = p === mainPersona;
                    if (pct === 0) return null; // Skip 0% matches to keep it clean
                    return (
                        <div key={p}>
                            <div className="flex justify-between text-xs font-bold mb-1">
                                <span className={isMain ? "text-[#F2C94C]" : "text-gray-400"}>{p}</span>
                                <span className={isMain ? "text-[#F2C94C]" : "text-gray-400"}>{pct}%</span>
                            </div>
                            <div className="w-full bg-black/40 rounded-full h-1.5">
                                <div
                                    className={`h-1.5 rounded-full ${isMain ? "bg-[#F2C94C]" : "bg-gray-600"}`}
                                    style={{ width: `${pct}%` }}
                                />
                            </div>
                        </div>
                    )
                })}
            </div>

            <div className="space-y-4">
                <ShareButton mainPersona={mainPersona} scores={scores} totalPoints={totalPoints} />
                <Link href="/friends" className="block w-full py-3 bg-transparent border-2 border-white/10 hover:border-white/30 text-gray-400 font-bold rounded-xl transition-all">
                    Try Again
                </Link>
            </div>
        </div>
    );
}

function ShareButton({ mainPersona, scores, totalPoints }: { mainPersona: string, scores: Record<string, number>, totalPoints: number }) {
    const [copied, setCopied] = useState(false);

    const handleShare = () => {
        // Find secondary persona
        const sorted = Object.entries(scores).sort(([, a], [, b]) => b - a);
        const secondary = sorted[1] && sorted[1][1] > 0 ? sorted[1][0] : null;

        const emojis: Record<string, string> = { Joey: '🍕', Monica: '🧼', Ross: '🦖', Chandler: '🛁', Rachel: '👗', Phoebe: '🎸' };

        let text = `🍕 *Friends Personality Quiz*\n\n`;
        text += `I am **${mainPersona}** ${emojis[mainPersona] || ''}!\n`;
        if (secondary) {
            text += `(and a little bit ${secondary} ${emojis[secondary] || ''})\n`;
        }
        text += `\nWho are you?\n👉 http://localhost:3000/friends`; // In prod use actual URL

        navigator.clipboard.writeText(text);
        setCopied(true);
        setTimeout(() => setCopied(false), 2000);
    };

    return (
        <button
            onClick={handleShare}
            className={`w-full py-3 font-bold rounded-xl transition-all shadow-lg flex items-center justify-center gap-2 ${copied ? 'bg-green-500 text-white' : 'bg-[#7B538C] hover:bg-[#6a467a] text-white'}`}
        >
            {copied ? (
                <><span>✅</span> Copied to Clipboard!</>
            ) : (
                <><span>📤</span> Share Results</>
            )}
        </button>
    );
}

export default function FriendsResult() {
    return (
        <div className="min-h-screen bg-[#7B538C] flex flex-col items-center justify-center p-6 font-sans">
            <Suspense fallback={<div className="text-white">Loading Results...</div>}>
                <ResultContent />
            </Suspense>
        </div>
    );
}
