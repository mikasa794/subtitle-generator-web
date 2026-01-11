'use client';

import { useState } from 'react';
import Link from 'next/link';

export default function ImportPage() {
    const [url, setUrl] = useState('');
    const [status, setStatus] = useState<'idle' | 'scanning' | 'importing' | 'success' | 'error'>('idle');
    const [logs, setLogs] = useState('');
    const [playlist, setPlaylist] = useState<any>(null); // { title, videos: [] }
    const [selectedIds, setSelectedIds] = useState<Set<string>>(new Set());
    const [importQueue, setImportQueue] = useState<string[]>([]);
    const [progress, setProgress] = useState({ current: 0, total: 0 });

    const isPlaylistUrl = url.includes('list=');

    const handleScanPlaylist = async () => {
        if (!url) return;
        setStatus('scanning');
        setLogs('🔍 Scanning Playlist...');
        setPlaylist(null);

        try {
            const res = await fetch('/api/playlist', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ url })
            });
            const data = await res.json();

            if (res.ok) {
                setPlaylist(data);
                setStatus('idle');
                setLogs(`✅ Found Playlist: ${data.title}\n${data.videos.length} videos available.`);
                // Select all by default
                setSelectedIds(new Set(data.videos.map((v: any) => v.id)));
            } else {
                setStatus('error');
                setLogs(`❌ Error scanning playlist: ${data.details || data.error}`);
            }
        } catch (e: any) {
            setStatus('error');
            setLogs(`❌ Network Error: ${e.message}`);
        }
    };

    const runImport = async (targetUrl: string) => {
        const res = await fetch('/api/import', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ url: targetUrl })
        });
        return res.json();
    };

    const handleBatchImport = async () => {
        if (!playlist || selectedIds.size === 0) return;

        const targets = playlist.videos.filter((v: any) => selectedIds.has(v.id));
        setStatus('importing');
        setProgress({ current: 0, total: targets.length });
        setLogs('🚀 Starting Batch Import...');

        let successCount = 0;
        let failCount = 0;

        for (let i = 0; i < targets.length; i++) {
            const video = targets[i];
            setLogs(prev => prev + `\n\n[${i + 1}/${targets.length}] Importing: ${video.title}...`);

            try {
                const result = await runImport(video.url);
                if (result.success) {
                    setLogs(prev => prev + `\n✅ Done.`);
                    successCount++;
                } else {
                    setLogs(prev => prev + `\n❌ Failed: ${result.error || 'Unknown'}`);
                    console.error(result);
                    failCount++;
                }
            } catch (e) {
                setLogs(prev => prev + `\n❌ Exception.`);
                failCount++;
            }
            setProgress({ current: i + 1, total: targets.length });
        }

        setStatus('success');
        setLogs(prev => prev + `\n\n🎉 Batch Complete! Success: ${successCount}, Failed: ${failCount}`);
    };

    const handleSingleImport = async () => {
        if (!url) return;
        setStatus('importing');
        setLogs('🚀 Starting Magic Import...\nThis may take 2-5 minutes depending on video length.\nPlease wait...');
        try {
            const data = await runImport(url);
            if (data.success) {
                setStatus('success');
                setLogs(data.logs);
            } else {
                setStatus('error');
                setLogs(`❌ Error: ${data.error}\nDetails: ${data.details}\nLogs: ${data.logs}`);
            }
        } catch (e: any) {
            setStatus('error');
            setLogs(`❌ Network Error: ${e.message}`);
        }
    };

    const toggleSelection = (id: string) => {
        const newSet = new Set(selectedIds);
        if (newSet.has(id)) newSet.delete(id);
        else newSet.add(id);
        setSelectedIds(newSet);
    };

    return (
        <div className="min-h-screen bg-[#F5F5F7] text-[#1d1d1f] p-8 font-sans">
            <header className="max-w-4xl mx-auto mb-8">
                <Link href="/lingo" className="text-sm text-gray-500 hover:text-[#1d1d1f] transition-colors mb-4 block">
                    ← Back to LingoTube
                </Link>
                <h1 className="text-3xl font-bold text-[#1d1d1f] tracking-tight">Creator Center</h1>
                <p className="text-gray-500 mt-2">Add new content to your library.</p>
            </header>

            <div className="max-w-4xl mx-auto space-y-6">

                {/* Input Section */}
                <div className="bg-white p-8 rounded-[20px] shadow-sm border border-gray-100">
                    <label className="block text-sm font-semibold mb-2 text-gray-700">YouTube URL</label>
                    <p className="text-xs text-gray-500 mb-4 bg-gray-50 p-2 rounded border border-gray-100 inline-block">
                        Supported: <span className="text-gray-900 font-medium">Single Video</span> (watch?v=...) or <span className="text-gray-900 font-medium">Playlist</span> (playlist?list=...).
                        <br />Playlists will unlock the batch scanner.
                    </p>
                    <div className="flex gap-4">
                        <input
                            type="text"
                            className="flex-1 bg-gray-50 border border-gray-200 rounded-xl p-3 text-gray-900 focus:outline-none focus:ring-2 focus:ring-teal-500/20 focus:border-teal-500 transition placeholder-gray-400"
                            placeholder="https://www.youtube.com/watch?v=... or https://www.youtube.com/playlist?list=..."
                            value={url}
                            onChange={(e) => setUrl(e.target.value)}
                            disabled={status === 'importing' || status === 'scanning'}
                        />

                        {isPlaylistUrl ? (
                            <button
                                onClick={handleScanPlaylist}
                                disabled={status === 'scanning' || status === 'importing'}
                                className="px-6 py-3 rounded-xl font-semibold bg-blue-600 hover:bg-blue-700 text-white transition disabled:opacity-50 shadow-sm"
                            >
                                {status === 'scanning' ? 'Scanning...' : 'Scan Payload'}
                            </button>
                        ) : (
                            <button
                                onClick={handleSingleImport}
                                disabled={status === 'importing' || !url}
                                className="px-6 py-3 rounded-xl font-semibold bg-[#1d1d1f] hover:bg-gray-800 text-white transition disabled:opacity-50 shadow-sm"
                            >
                                {status === 'importing' ? 'Importing...' : 'Start Import'}
                            </button>
                        )}
                    </div>
                </div>

                {/* Playlist Selection Area */}
                {playlist && (
                    <div className="bg-white p-6 rounded-[20px] shadow-sm border border-gray-100 animate-in fade-in slide-in-from-top-4">
                        <div className="flex justify-between items-center mb-6 border-b border-gray-100 pb-4">
                            <div>
                                <h2 className="text-xl font-bold text-gray-900">{playlist.title}</h2>
                                <p className="text-sm text-gray-500">{playlist.videos.length} videos found</p>
                            </div>
                            <div className="flex gap-2">
                                <button onClick={() => setSelectedIds(new Set(playlist.videos.map((v: any) => v.id)))} className="px-3 py-1 text-xs font-medium bg-gray-100 hover:bg-gray-200 text-gray-700 rounded-full transition">Select All</button>
                                <button onClick={() => setSelectedIds(new Set())} className="px-3 py-1 text-xs font-medium bg-gray-100 hover:bg-gray-200 text-gray-700 rounded-full transition">Clear</button>
                            </div>
                        </div>

                        <div className="max-h-96 overflow-y-auto mb-6 pr-2 space-y-2 custom-scrollbar">
                            {playlist.videos.map((video: any) => (
                                <div key={video.id}
                                    onClick={() => toggleSelection(video.id)}
                                    className={`p-3 rounded-xl border cursor-pointer flex items-center justify-between transition group
                                        ${selectedIds.has(video.id) ? 'bg-teal-50 border-teal-200 hover:border-teal-300' : 'bg-white border-gray-100 hover:border-gray-300 hover:shadow-sm'}
                                     `}>
                                    <div className="flex items-center gap-3 overflow-hidden">
                                        <div className={`w-5 h-5 rounded-md border flex items-center justify-center transition-colors ${selectedIds.has(video.id) ? 'bg-teal-500 border-teal-500' : 'border-gray-300 bg-white'}`}>
                                            {selectedIds.has(video.id) && <svg className="w-3 h-3 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth={3} d="M5 13l4 4L19 7" /></svg>}
                                        </div>
                                        <span className={`truncate text-sm font-medium ${selectedIds.has(video.id) ? 'text-teal-900' : 'text-gray-700'}`}>{video.title}</span>
                                    </div>
                                    <span className="text-xs text-gray-400 font-mono bg-gray-50 px-2 py-1 rounded">{Math.floor(video.duration / 60)}:{(video.duration % 60).toString().padStart(2, '0')}</span>
                                </div>
                            ))}
                        </div>

                        <div className="flex justify-between items-center border-t border-gray-100 pt-4">
                            <span className="text-gray-500 text-sm font-medium">Selected: {selectedIds.size}</span>
                            <button
                                onClick={handleBatchImport}
                                disabled={selectedIds.size === 0 || status === 'importing'}
                                className="px-8 py-2.5 rounded-xl font-bold bg-[#1d1d1f] hover:bg-gray-800 text-white disabled:opacity-50 transition shadow-sm"
                            >
                                {status === 'importing' ? `Running Batch (${progress.current}/${progress.total})...` : `Import ${selectedIds.size} Videos`}
                            </button>
                        </div>
                    </div>
                )}

                {/* Logs Area */}
                <div className="bg-[#1c1c1e] p-6 rounded-[20px] shadow-lg border border-gray-800 font-mono text-xs whitespace-pre-wrap h-80 overflow-y-auto">
                    <div className="flex justify-between mb-4 border-b border-white/10 pb-2">
                        <span className="text-gray-400 uppercase tracking-wider font-semibold text-[10px]">Console Output</span>
                        {status === 'importing' && <span className="text-teal-400 animate-pulse flex items-center gap-2"><span>●</span> Processing</span>}
                    </div>
                    <div className={status === 'error' ? 'text-red-400' : 'text-gray-300'}>
                        {logs || 'System Ready.'}
                    </div>
                </div>
            </div>
        </div>
    );
}
