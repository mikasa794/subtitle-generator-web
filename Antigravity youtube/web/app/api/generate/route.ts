import { NextResponse } from 'next/server';
import { exec } from 'child_process';
import path from 'path';

export async function POST(req: Request) {
    try {
        const { topic } = await req.json();

        if (!topic) {
            return NextResponse.json({ error: 'Topic is required' }, { status: 400 });
        }

        // Script path: ../src/generate_course.py relative to web/ directory
        // In production this pathing is fragile, but for local prototype it works.
        const scriptPath = path.resolve(process.cwd(), '../src/generate_course.py');

        console.log(`[API] Generating course for topic: "${topic}"...`);

        // Execute Python script
        // Note: This waits for completion. This might take 1-2 minutes.
        // If it times out, we might need to spawn without waiting.
        const command = `python "${scriptPath}" "${topic}"`;

        return new Promise<NextResponse>((resolve) => {
            exec(command, (error, stdout, stderr) => {
                if (error) {
                    console.error(`[API] Error: ${error.message}`);
                    resolve(NextResponse.json({ error: 'Generation Failed', details: stderr }, { status: 500 }));
                    return;
                }

                console.log(`[API] Success: ${stdout}`);
                resolve(NextResponse.json({ message: 'Course Generated Successfully', output: stdout }));
            });
        });

    } catch (error) {
        return NextResponse.json({ error: 'Internal Server Error' }, { status: 500 });
    }
}
