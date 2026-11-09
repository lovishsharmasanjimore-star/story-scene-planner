# Story Scene Planner

Turn a plain-text story into a structured scene plan and reusable image/video prompt brief.

## What it does
- Splits a story into scenes using paragraph or sentence mode.
- Estimates scene duration from narration word count and a configurable speaking rate.
- Exports JSON that can feed a video-rendering workflow.
- Produces prompt briefs; it does **not** call an image/video generation API.

## Run
```bash
python src/scene_planner.py story.txt --output scenes.json --words-per-minute 120
```
Optional: `--max-words 35` controls the approximate narration length per scene.

## Example
Input: paragraphs in `examples/story.txt`. Output schema is shown in `examples/scenes.example.json`.

## Roadmap
- [ ] Hindi-aware sentence segmentation improvements
- [ ] Character continuity bible
- [ ] Optional LLM adapter configured with the user's own API key

Python 3.10+, standard library only.
