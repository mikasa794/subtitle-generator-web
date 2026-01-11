
import { NextResponse } from 'next/server';
import { getVocabList } from '@/lib/feishu';

export async function GET() {
    const result = await getVocabList();
    if (result.success) {
        return NextResponse.json(result); // { success: true, items: [...] }
    } else {
        return NextResponse.json({ error: result.error }, { status: 500 });
    }
}
