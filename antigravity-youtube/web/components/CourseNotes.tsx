'use client';

import { useState, useEffect } from 'react';
import { Sparkles, Save, Loader2, FileText, Check } from 'lucide-react';

interface Props {
    courseTitle: string;
    lessonTitle: string;
    lessonId: string;
}

export default function CourseNotes({ courseTitle, lessonTitle, lessonId }: Props) {
    const [notes, setNotes] = useState('');
    const [isGenerating, setIsGenerating] = useState(false);
    const [saveStatus, setSaveStatus] = useState<'idle' | 'saving' | 'saved'>('idle');

    // Load notes from localStorage on mount or when lessonId changes
    useEffect(() => {
        const savedNotes = localStorage.getItem(`notes_${lessonId}`);
        if (savedNotes) {
            setNotes(savedNotes);
        } else {
            setNotes('');
        }
    }, [lessonId]);

    // Auto-save notes to localStorage
    useEffect(() => {
        const timer = setTimeout(() => {
            if (notes) {
                localStorage.setItem(`notes_${lessonId}`, notes);
                setSaveStatus('saved');
                setTimeout(() => setSaveStatus('idle'), 2000);
            }
        }, 1000);

        return () => clearTimeout(timer);
    }, [notes, lessonId]);

    const handleGenerateSummary = async () => {
        setIsGenerating(true);
        try {
            const res = await fetch('/api/summary', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ courseTitle, lessonTitle }),
            });
            const data = await res.json();

            if (data.summary && Array.isArray(data.summary)) {
                const summaryText = `\n\n### 🤖 AI Key Takeaways\n` + data.summary.map((s: string) => `- ${s}`).join('\n');

                // Append to existing notes
                const newNotes = notes + summaryText;
                setNotes(newNotes);
                localStorage.setItem(`notes_${lessonId}`, newNotes);
            } else {
                alert('Failed to generate summary.');
            }
        } catch (e) {
            console.error(e);
            alert('Error connecting to AI.');
        } finally {
            setIsGenerating(false);
        }
    };

    return (
        <div className="mt-8 bg-white border border-gray-200 rounded-2xl overflow-hidden shadow-sm">
            <div className="bg-gray-50 px-6 py-4 border-b border-gray-200 flex justify-between items-center">
                <h3 className="font-semibold text-gray-900 flex items-center gap-2">
                    <FileText className="w-4 h-4 text-gray-500" />
                    My Smart Notes
                </h3>
                <div className="flex items-center gap-3">
                    <span className="text-xs text-gray-400 font-medium flex items-center gap-1 min-w-[60px] justify-end">
                        {saveStatus === 'saved' && <><Check className="w-3 h-3" /> Saved</>}
                        {saveStatus === 'saving' && 'Saving...'}
                    </span>
                    <button
                        onClick={handleGenerateSummary}
                        disabled={isGenerating}
                        className="bg-purple-100 hover:bg-purple-200 text-purple-700 px-3 py-1.5 rounded-lg text-sm font-medium transition flex items-center gap-2 disabled:opacity-50"
                    >
                        {isGenerating ? <Loader2 className="w-3.5 h-3.5 animate-spin" /> : <Sparkles className="w-3.5 h-3.5" />}
                        Generate Takeaways
                    </button>
                </div>
            </div>
            <div className="p-0">
                <textarea
                    value={notes}
                    onChange={(e) => {
                        setNotes(e.target.value);
                        setSaveStatus('saving');
                    }}
                    className="w-full h-64 p-6 resize-none focus:outline-none focus:ring-0 text-gray-700 leading-relaxed"
                    placeholder="Type your notes here... Click 'Generate Takeaways' to get AI insights."
                />
            </div>
            <div className="bg-gray-50 px-6 py-2 border-t border-gray-100 text-xs text-gray-400 flex justify-between">
                <span>Markdown supported</span>
                <span>Stored locally on this device</span>
            </div>
        </div>
    );
}
