const fs = require('fs');
const path = require('path');
const OpenAI = require('openai');
const yaml = require('js-yaml');
const { GoogleGenerativeAI } = require("@google/generative-ai");

// Load config
const configPath = path.join(__dirname, '../config/sources.yaml');
let config;
try {
    const fileContents = fs.readFileSync(configPath, 'utf8');
    config = yaml.load(fileContents);
} catch (e) {
    console.error("Error loading config:", e);
    process.exit(1);
}

async function runGemini(apiKey, courseTitle, lessonTitle, systemPrompt) {
    const genAI = new GoogleGenerativeAI(apiKey);
    const model = genAI.getGenerativeModel({ model: "gemini-pro" });

    const finalPrompt = systemPrompt
        .replace('{{COURSE_TITLE}}', courseTitle)
        .replace('{{LESSON_TITLE}}', lessonTitle);

    const result = await model.generateContent([finalPrompt]);
    const response = await result.response;
    return response.text();
}

async function runOpenAI(apiKey, baseUrl, courseTitle, lessonTitle, systemPrompt) {
    const openai = new OpenAI({ apiKey: apiKey, baseURL: baseUrl });
    const finalPrompt = systemPrompt
        .replace('{{COURSE_TITLE}}', courseTitle)
        .replace('{{LESSON_TITLE}}', lessonTitle);

    const completion = await openai.chat.completions.create({
        messages: [
            { role: "system", content: "You are a helpful assistant that outputs JSON." },
            { role: "user", content: finalPrompt }
        ],
        model: "deepseek-chat",
        response_format: { type: "json_object" }
    });
    return completion.choices[0].message.content;
}

async function main() {
    const courseTitle = process.argv[2];
    const lessonTitle = process.argv[3];

    if (!courseTitle || !lessonTitle) {
        console.error("Usage: node generate_quiz.js \"<Course>\" \"<Lesson>\"");
        process.exit(1);
    }

    try {
        const promptPath = path.join(__dirname, '../config/quiz-prompt.md');
        const systemPrompt = fs.readFileSync(promptPath, 'utf8');

        let output = "";

        // PRIORITIZE GEMINI IF KEY EXISTS
        if (config.api_keys.google_api_key && config.api_keys.google_api_key.length > 10) {
            output = await runGemini(config.api_keys.google_api_key, courseTitle, lessonTitle, systemPrompt);
        } else if (config.api_keys.openai) {
            output = await runOpenAI(config.api_keys.openai, config.api_keys.openai_base_url, courseTitle, lessonTitle, systemPrompt);
        } else {
            throw new Error("No valid API Key found (OpenAI or Google) in sources.yaml");
        }

        // Clean output if it contains markdown code blocks
        let cleanOutput = output.trim();
        if (cleanOutput.startsWith('```json')) {
            cleanOutput = cleanOutput.substring(7);
        }
        if (cleanOutput.endsWith('```')) {
            cleanOutput = cleanOutput.substring(0, cleanOutput.length - 3);
        }

        console.log(cleanOutput);

    } catch (error) {
        // Output a simplified error JSON for the frontend to handle gracefully if needed, 
        // or just log error to stderr
        console.error("Error during AI processing:", error);
        process.exit(1);
    }
}

main();
