import { NextResponse } from 'next/server';
import { spawn } from 'child_process';
import path from 'path';

export async function POST(req: Request) {
    try {
        const { url } = await req.json();

        if (!url) {
            return NextResponse.json({ error: 'URL is required' }, { status: 400 });
        }

        const projectRoot = path.resolve(process.cwd(), '..');
        const scriptPath = path.join(projectRoot, 'src', 'magic_import.py');

        console.log(`Fetching playlist info for: ${url}`);

        return new Promise((resolve) => {
            // Run magic_import with --mode playlist
            const pythonProcess = spawn('python', [scriptPath, url, '--mode', 'playlist'], {
                cwd: projectRoot,
            });

            let outputData = '';
            let errorData = '';

            pythonProcess.stdout.on('data', (data) => {
                outputData += data.toString();
            });

            pythonProcess.stderr.on('data', (data) => {
                errorData += data.toString();
                console.error(`Python stderr: ${data}`);
            });

            pythonProcess.on('close', (code) => {
                if (code !== 0) {
                    resolve(NextResponse.json({ error: 'Failed to fetch playlist', details: errorData }, { status: 500 }));
                } else {
                    try {
                        const jsonData = JSON.parse(outputData);
                        resolve(NextResponse.json(jsonData));
                    } catch (e) {
                        resolve(NextResponse.json({ error: 'Invalid JSON from script', output: outputData }, { status: 500 }));
                    }
                }
            });
        });

    } catch (error) {
        console.error('API Error:', error);
        return NextResponse.json({ error: 'Internal Server Error' }, { status: 500 });
    }
}
