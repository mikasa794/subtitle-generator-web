
import { NextRequest, NextResponse } from 'next/server';
import { saveVocab } from '@/lib/feishu';

export async function POST(req: NextRequest) {
    try {
        const body = await req.json();
        console.log("📝 [API] Vocab Save Payload:", JSON.stringify(body, null, 2)); // Debug Log
        const { word, meaning, context, videoTitle, videoUrl, timestamp } = body;

        if (!word || !videoUrl) {
            console.error("❌ [API] Missing Fields:", { word, videoUrl });
            return NextResponse.json({ error: 'Missing required fields' }, { status: 400 });
        }

        const result = await saveVocab({
            word,
            meaning: meaning || '',
            context: context || '',
            videoTitle: videoTitle || 'LingoTube Video',
            videoUrl: videoUrl,
            timestamp: timestamp || 0
        });

        if (result.success) {
            return NextResponse.json({ success: true, id: result.id });
        } else {
            return NextResponse.json({ error: result.error }, { status: 500 });
        }
    } catch (e) {
        console.error('API Error:', e);
        return NextResponse.json({ error: 'Internal Server Error' }, { status: 500 });
    }
}
