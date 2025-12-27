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

async function runGemini(apiKey, transcript, systemPrompt) {
    const genAI = new GoogleGenerativeAI(apiKey);
    const model = genAI.getGenerativeModel({ model: "gemini-pro" });

    const result = await model.generateContent([
        systemPrompt,
        "\n\nHere is the content to adapt:\n",
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
            { role: "user", content: `Here is the content to adapt:\n\n${transcript}` }
        ],
        model: "deepseek-chat", // Default to deepseek, or whatever user has
    });
    return completion.choices[0].message.content;
}

async function main() {
    // Input is passed as argument or stdin
    const transcriptionPath = process.argv[2];
    const promptFilePath = process.argv[3]; // Optional: Custom prompt file

    let transcript = "";
    if (transcriptionPath) {
        transcript = fs.readFileSync(transcriptionPath, 'utf8');
    } else {
        // Fallback or error
        console.error("Usage: node ai_podcast_gen.js <path_to_content> [path_to_prompt]");
        process.exit(1);
    }

    try {
        // Default to english prompt if not specified
        const defaultPromptPath = path.join(__dirname, '../config/podcast-prompt.md');
        const finalPromptPath = promptFilePath ? promptFilePath : defaultPromptPath;

        const systemPrompt = fs.readFileSync(finalPromptPath, 'utf8');

        let output = "";

        // PRIORITIZE GEMINI IF KEY EXISTS
        if (config.api_keys.google_api_key && config.api_keys.google_api_key.length > 10) {
            output = await runGemini(config.api_keys.google_api_key, transcript, systemPrompt);
        } else if (config.api_keys.openai) {
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
