import os
import sys
import re
import asyncio
import subprocess
import yaml
import edge_tts

# Configuration
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ARCHIVES_DIR = os.path.join(BASE_DIR, 'archives')
WEB_PUBLIC_DIR = os.path.join(BASE_DIR, 'web', 'public')
OUTPUT_FILE = os.path.join(WEB_PUBLIC_DIR, 'podcast_demo.mp3')

# Voice Mapping
VOICE_ALEX = "en-US-GuyNeural" # Male
VOICE_JAMIE = "en-US-JennyNeural" # Female

# For Chinese Content Support (Auto-detect later if needed, but for now hardcode logic)
# Actually, the user's content is likely Chinese (based on recent interactions).
# The Prompt asks for "Alex" and "Jamie" but the content is Chinese.
# We should probably use Chinese Voices if the prompt generates Chinese. 
# But the prompt I wrote asks for "Hello and welcome back". 
# Let's adjust the prompt separately if needed, but for now let's assume the LLM follows language of input or prompt.
# Given the user's "Denoise" site is Chinese, the podcast should likely be Chinese.
# Let's simple check: if text contains Chinese characters, use Chinese voices.
VOICE_ZH_MALE = "zh-CN-YunxiNeural"
VOICE_ZH_FEMALE = "zh-CN-XiaoxiaoNeural"

def is_chinese(text):
    return re.search(u'[\u4e00-\u9fff]', text)

def get_latest_content():
    """Finds the most recent text file in archives."""
    # Recursively find all text files in archives
    latest_file = None
    latest_time = 0
    
    for root, dirs, files in os.walk(ARCHIVES_DIR):
        for f in files:
            if f == 'rewritten.md' or f.endswith('.md'): # Prefer rewrite content
                full_path = os.path.join(root, f)
                mtime = os.path.getmtime(full_path)
                if mtime > latest_time:
                    latest_time = mtime
                    latest_file = full_path
    
    return latest_file

def generate_script(content_path, prompt_file):
    print(f"Generating podcast script using prompt: {prompt_file}...")
    node_script = os.path.join(BASE_DIR, 'src', 'ai_podcast_gen.js')
    result = subprocess.run(
        ['node', node_script, content_path, prompt_file],
        capture_output=True, text=True, encoding='utf-8'
    )
    if result.returncode != 0:
        raise Exception(f"AI Generation Failed: {result.stderr}")
    return result.stdout

# ... (previous code)

def parse_script(xml_content):
    # Remove markdown code blocks if any
    clean_content = re.sub(r'^```\w*\s*', '', xml_content.strip(), flags=re.MULTILINE)
    clean_content = re.sub(r'```$', '', clean_content.strip(), flags=re.MULTILINE)

    # Regex to find <line speaker="...">text</line>
    lines = []
    pattern = r'<line speaker="(.*?)">(.*?)</line>'
    matches = re.findall(pattern, clean_content, re.DOTALL)
    
    for speaker, text in matches:
        lines.append({
            "speaker": speaker,
            "text": text.strip()
        })
    return lines

# ... (rest of code)

async def synthesize_audio(lines, lang_voice_map):
    print(f"Synthesizing {len(lines)} lines of audio...")
    temp_files = []
    
    for idx, line in enumerate(lines):
        text = line['text']
        speaker = line['speaker']
        
        # Default Voice
        voice = lang_voice_map['male'] # Fallback
        
        # Simple heuristic mapping based on speaker name
        if any(name in speaker for name in ['Jamie', 'Li', 'Female']):
            voice = lang_voice_map['female']
        elif any(name in speaker for name in ['Alex', 'Zhang', 'Male']):
            voice = lang_voice_map['male']
            
        print(f"  [{idx+1}/{len(lines)}] {speaker} ({voice}): {text[:20]}...")
        
        communicate = edge_tts.Communicate(text, voice)
        temp_filename = os.path.join(BASE_DIR, f"temp_{idx}.mp3")
        await communicate.save(temp_filename)
        temp_files.append(temp_filename)
    
    return temp_files

def concat_mp3s(files, output_path):
    print(f"Concatenating to {output_path}...")
    with open(output_path, 'wb') as outfile:
        for f in files:
            with open(f, 'rb') as infile:
                outfile.write(infile.read())
            # Cleanup
            os.remove(f)

def run_pipeline(content_path, prompt_file, output_file, voice_map):
    print(f"\n--- Starting Pipeline for {output_file} ---")
    
    # 1. Generate Script
    xml_script = generate_script(content_path, prompt_file)
    
    # 2. Parse
    lines = parse_script(xml_script)
    if not lines:
        print("No dialogues parsed.")
        return

    # 3. Synthesize
    temp_files = asyncio.run(synthesize_audio(lines, voice_map))

    # 4. Concatenate
    concat_mp3s(temp_files, output_file)
    print(f"Saved to {output_file}")


def main():
    try:
        # 1. Get Content
        content_path = get_latest_content()
        if not content_path:
            print("No content found in archives.")
            return
        print(f"Found content: {content_path}")

        # Configs
        configs = [
            {
                "lang": "en",
                "prompt": os.path.join(BASE_DIR, 'config', 'podcast-prompt.md'),
                "output": os.path.join(WEB_PUBLIC_DIR, 'podcast_demo_en.mp3'),
                "voices": {"male": "en-US-GuyNeural", "female": "en-US-JennyNeural"}
            },
            {
                "lang": "cn",
                "prompt": os.path.join(BASE_DIR, 'config', 'podcast-prompt-cn.md'),
                "output": os.path.join(WEB_PUBLIC_DIR, 'podcast_demo_cn.mp3'),
                "voices": {"male": "zh-CN-YunxiNeural", "female": "zh-CN-XiaoxiaoNeural"}
            }
        ]

        for cfg in configs:
            run_pipeline(content_path, cfg['prompt'], cfg['output'], cfg['voices'])

        print("\nAll podcasts generated.")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
