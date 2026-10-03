import unittest
from long_context_lab.needles import make_task
from long_context_lab.windows import windows, locate


class Tests(unittest.TestCase):
    def test_task_contains_answer(self):
        task = make_task(1000, .5, "x")
        self.assertIn(task.answer, task.prompt)

    def test_windows_cover_text(self):
        parts = windows("abcdefghij", 6, 2)
        self.assertEqual(parts, ["abcdef", "efghij"])

    def test_locate(self):
        self.assertGreater(locate("abc target xyz", "target"), 0)


if __name__ == "__main__":
    unittest.main()
