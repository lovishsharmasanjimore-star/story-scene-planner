import sys, unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parents[1] / "src"))
from scene_planner import build_plan, split_story
class PlannerTests(unittest.TestCase):
    def test_empty_story_rejected(self):
        with self.assertRaises(ValueError): build_plan(" ")
    def test_plan_has_scenes(self):
        plan=build_plan("A boy finds a map. He follows it.", max_words=5)
        self.assertGreaterEqual(plan["scene_count"], 1)
        self.assertIn("duration_sec", plan["scenes"][0])
if __name__ == "__main__": unittest.main()
