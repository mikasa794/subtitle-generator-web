import { NextResponse } from 'next/server';
import { exec } from 'child_process';
import path from 'path';

export async function POST(request: Request) {
    try {
        const { courseTitle, lessonTitle } = await request.json();

        if (!courseTitle || !lessonTitle) {
            return NextResponse.json({ error: 'Missing courseTitle or lessonTitle' }, { status: 400 });
        }

        const scriptPath = path.resolve(process.cwd(), '../src/generate_summary.js');

        // Escape quotes to prevent shell injection (basic)
        const safeCourseTitle = courseTitle.replace(/"/g, '\\"');
        const safeLessonTitle = lessonTitle.replace(/"/g, '\\"');

        const command = `node "${scriptPath}" "${safeCourseTitle}" "${safeLessonTitle}"`;

        return new Promise<NextResponse>((resolve) => {
            exec(command, (error, stdout, stderr) => {
                if (error) {
                    console.error(`[API] Summary generation script error: ${stderr}`);
                    resolve(NextResponse.json({ error: 'Summary generation failed' }, { status: 500 }));
                    return;
                }

                try {
                    const result = JSON.parse(stdout.trim());
                    resolve(NextResponse.json(result));
                } catch (e) {
                    console.error(`[API] Failed to parse JSON: ${stdout}`);
                    resolve(NextResponse.json({ error: 'Invalid response from AI' }, { status: 500 }));
                }
            });
        });

    } catch (error) {
        return NextResponse.json({ error: 'Internal Server Error' }, { status: 500 });
    }
}
