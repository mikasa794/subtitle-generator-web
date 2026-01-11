import { NextResponse } from 'next/server';
import { spawn } from 'child_process';
import path from 'path';

export const maxDuration = 300; // 5 minutes timeout for Vercel/Next

export async function POST(req: Request) {
    try {
        const { topic } = await req.json();

        if (!topic) {
            return NextResponse.json(
                { error: 'Topic is required' },
                { status: 400 }
            );
        }

        const scriptPath = path.join(process.cwd(), '../src/generate_course.py');

        // Check if running on Vercel or local
        // On Vercel, this won't work easily because Python isn't there by default unless configured.
        // But since user is running LOCALLY, this works fine.

        return new Promise((resolve, reject) => {
            const pythonProcess = spawn('python', [scriptPath, topic]);

            let output = '';
            let error = '';

            pythonProcess.stdout.on('data', (data) => {
                output += data.toString();
                // Here we could stream logs if we used a streaming response
            });

            pythonProcess.stderr.on('data', (data) => {
                error += data.toString();
            });

            pythonProcess.on('close', (code) => {
                if (code !== 0) {
                    console.error(`Python Output: ${output}`);
                    console.error(`Python Error: ${error}`);
                    resolve(NextResponse.json({ error: 'Failed to generate course', details: error }, { status: 500 }));
                } else {
                    // Parse output to find something useful or just success
                    resolve(NextResponse.json({ success: true, message: 'Course generated', output }));
                }
            });
        });
    } catch (error) {
        console.error('API Error:', error);
        return NextResponse.json(
            { error: 'Internal Server Error' },
            { status: 500 }
        );
    }
}
