'use client';

import { useState } from 'react';
import { BrainCircuit, CheckCircle, XCircle, RefreshCw, Loader2, ArrowRight } from 'lucide-react';

interface Question {
    id: number;
    text: string;
    options: string[];
    correctIndex: number;
    explanation: string;
}

interface Props {
    courseTitle: string;
    lessonTitle: string;
}

export default function CourseQuiz({ courseTitle, lessonTitle }: Props) {
    const [status, setStatus] = useState<'idle' | 'loading' | 'active' | 'finished'>('idle');
    const [questions, setQuestions] = useState<Question[]>([]);
    const [currentIndex, setCurrentIndex] = useState(0);
    const [score, setScore] = useState(0);
    const [selectedOption, setSelectedOption] = useState<number | null>(null);
    const [isAnswered, setIsAnswered] = useState(false);

    const startQuiz = async () => {
        setStatus('loading');
        try {
            const res = await fetch('/api/quiz', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ courseTitle, lessonTitle }),
            });
            const data = await res.json();

            if (data.questions && Array.isArray(data.questions)) {
                setQuestions(data.questions);
                setStatus('active');
                setCurrentIndex(0);
                setScore(0);
                setIsAnswered(false);
                setSelectedOption(null);
            } else {
                alert('Failed to generate quiz. Please try again.');
                setStatus('idle');
            }
        } catch (e) {
            console.error(e);
            alert('Error connecting to AI.');
            setStatus('idle');
        }
    };

    const handleOptionClick = (index: number) => {
        if (isAnswered) return;
        setSelectedOption(index);
        setIsAnswered(true);

        if (index === questions[currentIndex].correctIndex) {
            setScore(s => s + 1);
        }
    };

    const nextQuestion = () => {
        if (currentIndex < questions.length - 1) {
            setCurrentIndex(c => c + 1);
            setIsAnswered(false);
            setSelectedOption(null);
        } else {
            setStatus('finished');
        }
    };

    if (status === 'idle') {
        return (
            <div className="mt-8 border-t border-gray-100 pt-8">
                <div className="bg-gradient-to-br from-indigo-50 to-purple-50 rounded-2xl p-6 flex items-center justify-between">
                    <div>
                        <h3 className="text-lg font-semibold text-indigo-900 flex items-center gap-2">
                            <BrainCircuit className="w-5 h-5" />
                            AI 随堂测验
                        </h3>
                        <p className="text-sm text-indigo-700/80 mt-1">
                            生成 3 道关于本节课的选择题，检测学习成果。
                        </p>
                    </div>
                    <button
                        onClick={startQuiz}
                        className="bg-indigo-600 hover:bg-indigo-700 text-white px-6 py-2 rounded-full font-medium transition shadow-lg shadow-indigo-200"
                    >
                        开始测验
                    </button>
                </div>
            </div>
        );
    }

    if (status === 'loading') {
        return (
            <div className="mt-8 p-8 text-center bg-gray-50 rounded-2xl">
                <Loader2 className="w-8 h-8 text-indigo-500 animate-spin mx-auto mb-3" />
                <p className="text-gray-500 text-sm">AI 正在出题中...</p>
            </div>
        );
    }

    if (status === 'finished') {
        return (
            <div className="mt-8 bg-white border border-gray-200 rounded-2xl p-8 text-center">
                <div className="inline-flex items-center justify-center w-16 h-16 rounded-full bg-green-100 text-green-600 mb-4">
                    <CheckCircle className="w-8 h-8" />
                </div>
                <h3 className="text-2xl font-bold text-gray-900 mb-2">测验完成!</h3>
                <p className="text-gray-600 mb-6">
                    你的得分: <span className="font-bold text-indigo-600 text-xl">{score} / {questions.length}</span>
                </p>
                <button
                    onClick={() => setStatus('idle')}
                    className="text-gray-500 hover:text-gray-900 flex items-center gap-2 mx-auto text-sm"
                >
                    <RefreshCw className="w-4 h-4" /> 再测一次
                </button>
            </div>
        );
    }

    // Active Question View
    const question = questions[currentIndex];
    const isCorrect = selectedOption === question.correctIndex;

    return (
        <div className="mt-8 bg-white border border-indigo-100 shadow-sm rounded-2xl overflow-hidden">
            <div className="bg-indigo-50/50 px-6 py-4 border-b border-indigo-100 flex justify-between items-center">
                <span className="text-xs font-bold text-indigo-400 uppercase tracking-wider">
                    Question {currentIndex + 1} / {questions.length}
                </span>
                <span className="text-sm font-medium text-gray-400">Score: {score}</span>
            </div>

            <div className="p-6">
                <h3 className="text-lg font-medium text-gray-900 mb-6 leading-relaxed">
                    {question.text}
                </h3>

                <div className="space-y-3">
                    {question.options.map((option, idx) => {
                        let btnClass = "w-full text-left p-4 rounded-xl border-2 transition-all duration-200 flex items-center justify-between group ";

                        if (isAnswered) {
                            if (idx === question.correctIndex) {
                                btnClass += "border-green-500 bg-green-50 text-green-700";
                            } else if (idx === selectedOption) {
                                btnClass += "border-red-500 bg-red-50 text-red-700";
                            } else {
                                btnClass += "border-gray-100 opacity-50";
                            }
                        } else {
                            btnClass += "border-gray-100 hover:border-indigo-200 hover:bg-indigo-50 hover:text-indigo-700";
                        }

                        return (
                            <button
                                key={idx}
                                onClick={() => handleOptionClick(idx)}
                                disabled={isAnswered}
                                className={btnClass}
                            >
                                <span className="font-medium">{option}</span>
                                {isAnswered && idx === question.correctIndex && <CheckCircle className="w-5 h-5 text-green-500" />}
                                {isAnswered && idx === selectedOption && idx !== question.correctIndex && <XCircle className="w-5 h-5 text-red-500" />}
                            </button>
                        );
                    })}
                </div>

                {isAnswered && (
                    <div className="mt-6 pt-6 border-t border-gray-100 animate-in fade-in slide-in-from-bottom-4">
                        <div className={`p-4 rounded-xl mb-4 ${isCorrect ? 'bg-green-50 text-green-800' : 'bg-red-50 text-red-800'}`}>
                            <p className="font-bold mb-1">{isCorrect ? 'Correct!' : 'Incorrect'}</p>
                            <p className="text-sm opacity-90">{question.explanation}</p>
                        </div>
                        <button
                            onClick={nextQuestion}
                            className="float-right bg-[#1D1D1F] text-white px-6 py-2 rounded-full font-medium hover:bg-black transition flex items-center gap-2"
                        >
                            {currentIndex < questions.length - 1 ? 'Next Question' : 'View Results'} <ArrowRight className="w-4 h-4" />
                        </button>
                    </div>
                )}
            </div>
        </div>
    );
}
