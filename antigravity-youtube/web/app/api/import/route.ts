import { NextResponse } from 'next/server';
import { exec } from 'child_process';
import path from 'path';
import { promisify } from 'util';

const execAsync = promisify(exec);

export async function POST(req: Request) {
    try {
        const body = await req.json();
        const { url } = body;

        if (!url) {
            return NextResponse.json({ error: 'URL is required' }, { status: 400 });
        }

        // Determine script path (web/../src/magic_import.py)
        const scriptPath = path.resolve(process.cwd(), '../src/magic_import.py');

        // Command to run python script
        // Assuming 'python' is in PATH. 
        // We use double quotes for URL to prevent shell injection issues, though basic.
        const command = `python "${scriptPath}" "${url}"`;

        console.log('🚀 Executing Magic Import:', command);

        // Execute
        const { stdout, stderr } = await execAsync(command);

        console.log('✅ Import Output:', stdout);
        if (stderr) console.error('⚠️ Import Stderr:', stderr);

        // Check for success marker or exit code (execAsync throws on non-zero exit)

        return NextResponse.json({
            success: true,
            message: 'Import completed successfully',
            logs: stdout
        });

    } catch (error: any) {
        console.error('❌ Import Failed:', error);
        return NextResponse.json({
            error: 'Import failed',
            details: error.message,
            logs: error.stdout || ''
        }, { status: 500 });
    }
}
