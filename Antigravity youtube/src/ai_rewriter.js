const fs = require('fs');
const path = require('path');
const OpenAI = require('openai');
const yaml = require('js-yaml');

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

const { GoogleGenerativeAI } = require("@google/generative-ai");

// ... (load config logic same as before)

async function runGemini(apiKey, transcript, systemPrompt) {
    const genAI = new GoogleGenerativeAI(apiKey);
    const model = genAI.getGenerativeModel({ model: "gemini-pro" });

    const result = await model.generateContent([
        systemPrompt,
        "\n\nHere is the transcript:\n",
        transcript
    ]);
    const response = await result.response;
    return response.text();
}

async function runOpenAI(apiKey, baseUrl, transcript, systemPrompt) {
    const openai = new OpenAI({ apiKey: apiKey, baseURL: baseUrl });
    const completion = await openai.chat.completions.create({
        messages: [
            { role: "system", content: systemPrompt },
            { role: "user", content: `Here is the transcript:\n\n${transcript}` }
        ],
        model: "deepseek-chat",
    });
    return completion.choices[0].message.content;
}

async function main() {
    const transcriptionPath = process.argv[2];
    if (!transcriptionPath) {
        console.error("Usage: node ai_rewriter.js <path_to_transcript>");
        process.exit(1);
    }

    try {
        const transcript = fs.readFileSync(transcriptionPath, 'utf8');
        const promptPath = path.join(__dirname, '../config/rewrite-prompt.md');
        const systemPrompt = fs.readFileSync(promptPath, 'utf8');

        let output = "";

        // PRIORITIZE GEMINI IF KEY EXISTS
        if (config.api_keys.google_api_key && config.api_keys.google_api_key.length > 10) {
            // console.error("Using Google Gemini...");
            output = await runGemini(config.api_keys.google_api_key, transcript, systemPrompt);
        } else if (config.api_keys.openai) {
            // console.error("Using OpenAI...");
            output = await runOpenAI(config.api_keys.openai, config.api_keys.openai_base_url, transcript, systemPrompt);
        } else {
            throw new Error("No valid API Key found (OpenAI or Google) in sources.yaml");
        }

        console.log(output);

    } catch (error) {
        console.error("Error during AI processing:", error);
        process.exit(1);
    }
}

main();
