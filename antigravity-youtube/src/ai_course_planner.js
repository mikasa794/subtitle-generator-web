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

async function runGemini(apiKey, topic, systemPrompt) {
    const genAI = new GoogleGenerativeAI(apiKey);
    const model = genAI.getGenerativeModel({ model: "gemini-pro" });

    const finalPrompt = systemPrompt.replace('{{TOPIC}}', topic);

    const result = await model.generateContent([finalPrompt]);
    const response = await result.response;
    return response.text();
}

async function runOpenAI(apiKey, baseUrl, topic, systemPrompt) {
    const openai = new OpenAI({ apiKey: apiKey, baseURL: baseUrl });
    const finalPrompt = systemPrompt.replace('{{TOPIC}}', topic);

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
    const topic = process.argv[2];
    if (!topic) {
        console.error("Usage: node ai_course_planner.js \"<topic>\"");
        process.exit(1);
    }

    try {
        const promptPath = path.join(__dirname, '../config/course-prompt.md');
        const systemPrompt = fs.readFileSync(promptPath, 'utf8');

        let output = "";

        // PRIORITIZE GEMINI IF KEY EXISTS
        if (config.api_keys.google_api_key && config.api_keys.google_api_key.length > 10) {
            output = await runGemini(config.api_keys.google_api_key, topic, systemPrompt);
        } else if (config.api_keys.openai) {
            output = await runOpenAI(config.api_keys.openai, config.api_keys.openai_base_url, topic, systemPrompt);
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
