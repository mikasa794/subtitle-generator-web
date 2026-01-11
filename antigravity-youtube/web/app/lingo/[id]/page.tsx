import { fetchLingoClips } from '@/lib/feishu';
import LingoPlayerClient from './LingoPlayer';

export const revalidate = 0;

interface PageProps {
    params: Promise<{ id: string }>;
}

export default async function LingoPlayerPage({ params }: { params: Promise<{ id: string }> }) {
    const resolvedParams = await params;
    const clips = await fetchLingoClips();
    const clip = clips.find(c => c.id === resolvedParams.id);

    if (!clip) {
        return <div className="p-8">Clip not found</div>;
    }

    // Pass data to Client Component
    return <LingoPlayerClient clip={clip} />;
}
