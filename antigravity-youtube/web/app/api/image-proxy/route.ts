import { NextRequest, NextResponse } from 'next/server';

const APP_ID = process.env.FEISHU_APP_ID || 'cli_a9c6a1bb56f89cd4';
const APP_SECRET = process.env.FEISHU_APP_SECRET || 'Ox6v51RIbon1bbxaHmvUGhqRNnW3CiUs';

async function getTenantAccessToken() {
    const res = await fetch('https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            app_id: APP_ID,
            app_secret: APP_SECRET,
        }),
        cache: 'no-store',
    });

    const data = await res.json();
    if (data.code !== 0) {
        throw new Error(`Failed to get access token: ${data.msg}`);
    }
    return data.tenant_access_token;
}

export async function GET(request: NextRequest) {
    const url = request.nextUrl.searchParams.get('url');

    if (!url) {
        return NextResponse.json({ error: 'Missing url parameter' }, { status: 400 });
    }

    try {
        const token = await getTenantAccessToken();
        const headers = {
            'Authorization': `Bearer ${token}`,
            // Some Feishu images might need Referer or User-Agent, but Bearer is usually enough for drive files
        };

        const response = await fetch(url, { headers });

        if (!response.ok) {
            return NextResponse.json({ error: `Failed to fetch image: ${response.statusText}` }, { status: response.status });
        }

        const contentType = response.headers.get('content-type') || 'application/octet-stream';
        const buffer = await response.arrayBuffer();

        return new NextResponse(buffer, {
            headers: {
                'Content-Type': contentType,
                'Cache-Control': 'public, max-age=31536000, immutable',
            },
        });
    } catch (error) {
        console.error('Image proxy error:', error);
        return NextResponse.json({ error: 'Internal server error' }, { status: 500 });
    }
}
