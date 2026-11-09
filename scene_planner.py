import argparse, json, re
from pathlib import Path

def split_story(text, max_words=35):
    paragraphs = [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip()]
    scenes = []
    for paragraph in paragraphs:
        sentences = re.split(r"(?<=[.!?।])\s+", paragraph)
        current = []
        count = 0
        for sentence in sentences:
            words = sentence.split()
            if current and count + len(words) > max_words:
                scenes.append(" ".join(current)); current=[]; count=0
            current.append(sentence); count += len(words)
        if current:
            scenes.append(" ".join(current))
    return scenes

def build_plan(text, words_per_minute=120, max_words=35):
    if words_per_minute <= 0 or max_words <= 0:
        raise ValueError("words_per_minute and max_words must be positive")
    chunks = split_story(text, max_words)
    if not chunks:
        raise ValueError("Story is empty")
    result = []
    for i, narration in enumerate(chunks, 1):
        words = len(narration.split())
        duration = max(3, round(words / words_per_minute * 60))
        result.append({
            "scene": i,
            "narration": narration,
            "duration_sec": duration,
            "image_prompt_brief": f"Illustrate this story moment: {narration}",
            "video_motion_brief": "Add subtle character movement and a slow cinematic camera move."
        })
    return {"title": "Untitled story", "scene_count": len(result), "scenes": result}

def main():
    p=argparse.ArgumentParser()
    p.add_argument("story", type=Path)
    p.add_argument("--output", type=Path, default=Path("scenes.json"))
    p.add_argument("--words-per-minute", type=int, default=120)
    p.add_argument("--max-words", type=int, default=35)
    a=p.parse_args()
    plan=build_plan(a.story.read_text(encoding="utf-8"), a.words_per_minute, a.max_words)
    a.output.write_text(json.dumps(plan, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote {plan['scene_count']} scenes to {a.output}")

if __name__ == "__main__": main()
