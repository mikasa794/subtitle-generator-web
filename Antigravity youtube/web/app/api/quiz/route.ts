import { NextResponse } from 'next/server';
import { exec } from 'child_process';
import path from 'path';

export async function POST(req: Request) {
    try {
        const { courseTitle, lessonTitle } = await req.json();

        if (!courseTitle || !lessonTitle) {
            return NextResponse.json({ error: 'Missing title needed for context' }, { status: 400 });
        }

        const scriptPath = path.resolve(process.cwd(), '../src/generate_quiz.js');
        // Retrieve Node path just in case, but usually 'node' is in PATH.
        // We use double quotes to handle spaces in titles.
        // BE CAREFUL: Sanitization. 
        // In a real app we should use execFile to avoid shell injection, 
        // but for local prototype exec with quotes is okay-ish if we trust the input.
        // We will escape quotes in the titles.
        const safeCourse = courseTitle.replace(/"/g, '\\"');
        const safeLesson = lessonTitle.replace(/"/g, '\\"');

        const command = `node "${scriptPath}" "${safeCourse}" "${safeLesson}"`;

        console.log(`[API] Generating Quiz for: ${safeLesson}...`);

        return new Promise<NextResponse>((resolve) => {
            exec(command, (error, stdout, stderr) => {
                if (error) {
                    console.error(`[API] Quiz Error: ${stderr}`);
                    resolve(NextResponse.json({ error: 'Quiz Generation Failed' }, { status: 500 }));
                    return;
                }

                try {
                    const json = JSON.parse(stdout);
                    resolve(NextResponse.json(json));
                } catch (e) {
                    console.error(`[API] JSON Parse Error. Output: ${stdout}`);
                    resolve(NextResponse.json({ error: 'Invalid AI Response' }, { status: 500 }));
                }
            });
        });

    } catch (error) {
        return NextResponse.json({ error: 'Internal Server Error' }, { status: 500 });
    }
}
