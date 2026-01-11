
import { NextRequest, NextResponse } from 'next/server';
import { getTenantAccessToken } from '@/lib/feishu';

const APP_TOKEN = process.env.FEISHU_APP_TOKEN || 'FCnWb734NawZW6spPVvcMjtonjf';
const VOCAB_TABLE_ID = 'tblx7DodiHH6jkVR'; // HARDCODED V3 TABLE (TEXT FIELDS)

export async function POST(req: NextRequest) {
    try {
        const body = await req.json();
        console.log("📝 [API V3] Save Payload:", JSON.stringify(body, null, 2));

        const { word, meaning, context, videoTitle, videoUrl, timestamp } = body;

        if (!word || !videoUrl) {
            return NextResponse.json({ error: 'Missing required fields' }, { status: 400 });
        }

        const token = await getTenantAccessToken();
        const url = `https://open.feishu.cn/open-apis/bitable/v1/apps/${APP_TOKEN}/tables/${VOCAB_TABLE_ID}/records`;

        const fields = {
            "Word": word,
            "Meaning": meaning || '',
            "Context Sentence": context || '',
            "Video Title": videoTitle || 'LingoTube Video',
            "Video URL": { link: videoUrl, text: "View Video" },
            "Timestamp": String(timestamp || 0), // TEXT FIELD
            "Saved Date": String(Date.now()),    // TEXT FIELD
            "Review Count": "0"                  // TEXT FIELD
        };

        console.log("📤 [API V2] Sending Fields:", JSON.stringify(fields, null, 2));

        const res = await fetch(url, {
            method: 'POST',
            headers: {
                'Authorization': `Bearer ${token}`,
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ fields })
        });

        const data = await res.json();

        if (data.code === 0) {
            return NextResponse.json({ success: true, id: data.data.record.record_id });
        } else {
            console.error('❌ [API V2] Feishu Error:', data);
            return NextResponse.json({ error: `Feishu Error: ${data.msg}` }, { status: 500 });
        }

    } catch (e: any) {
        console.error('❌ [API V2] Exception:', e);
        return NextResponse.json({ error: e.message || 'Internal Server Error' }, { status: 500 });
    }
}
