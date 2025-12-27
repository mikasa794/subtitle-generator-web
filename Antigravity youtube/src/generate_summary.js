const fs = require('fs');
const path = require('path');
const { GoogleGenerativeAI } = require('@google/generative-ai');
const OpenAI = require('openai');
const yaml = require('js-yaml');

// 1. Config
const CONFIG_DIR = path.join(__dirname, '../config');
const SOURCES_PATH = path.join(CONFIG_DIR, 'sources.yaml');
const PROMPT_PATH = path.join(CONFIG_DIR, 'summary-prompt.md');

// 2. Parse Args
const courseTitle = process.argv[2];
const lessonTitle = process.argv[3];

if (!courseTitle || !lessonTitle) {
    console.error('Usage: node generate_summary.js "<course_title>" "<lesson_title>"');
    process.exit(1);
}

async function runGemini(apiKey, prompt) {
    const genAI = new GoogleGenerativeAI(apiKey);
    const model = genAI.getGenerativeModel({ model: "gemini-pro" });
    const result = await model.generateContent(prompt);
    const response = await result.response;
    return response.text();
}

async function runOpenAI(apiKey, baseUrl, prompt) {
    const openai = new OpenAI({ apiKey: apiKey, baseURL: baseUrl });
    const completion = await openai.chat.completions.create({
        messages: [
            { role: "system", content: "You are a helpful assistant that outputs JSON." },
            { role: "user", content: prompt }
        ],
        model: "deepseek-chat",
        response_format: { type: "json_object" }
    });
    return completion.choices[0].message.content;
}

async function main() {
    try {
        // Load Config
        let config;
        try {
            config = yaml.load(fs.readFileSync(SOURCES_PATH, 'utf8'));
        } catch (e) {
            console.error("Error loading config:", e);
            process.exit(1);
        }

        // Load Prompt
        let promptTemplate = fs.readFileSync(PROMPT_PATH, 'utf8');
        const prompt = promptTemplate
            .replace('{{COURSE_TITLE}}', courseTitle)
            .replace('{{LESSON_TITLE}}', lessonTitle);

        let resultText = '';
        const apiKeys = config.api_keys;

        // Prioritize Gemini if invalid key check passes (length > 10)
        // Note: The yaml might have placeholder 'YOUR_GEMINI_API_KEY' which is > 10 chars but invalid.
        // But assuming user has set it or using OpenAI.

        if (apiKeys.google_api_key && apiKeys.google_api_key.length > 20 && !apiKeys.google_api_key.includes('YOUR_')) {
            resultText = await runGemini(apiKeys.google_api_key, prompt);
        } else if (apiKeys.openai && !apiKeys.openai.includes('YOUR_')) {
            resultText = await runOpenAI(apiKeys.openai, apiKeys.openai_base_url, prompt);
        } else if (apiKeys.gemini && apiKeys.gemini.length > 20 && !apiKeys.gemini.includes('YOUR_')) {
            // Fallback to checking 'gemini' key directly if google_api_key was empty but this exists
            resultText = await runGemini(apiKeys.gemini, prompt);
        } else {
            // Try valid ones even if they look like placeholders if we are desperate, but better to throw
            if (apiKeys.openai) {
                // Fallback to OpenAI if key exists (even if short/suspicious, let the lib fail)
                resultText = await runOpenAI(apiKeys.openai, apiKeys.openai_base_url, prompt);
            } else {
                throw new Error('No valid API Key found (OpenAI or Google) in sources.yaml');
            }
        }

        // Clean output
        resultText = resultText.replace(/```json\n?|\n?```/g, '').trim();

        console.log(resultText);

    } catch (error) {
        console.error('Error generating summary:', error);
        process.exit(1);
    }
}

main();
