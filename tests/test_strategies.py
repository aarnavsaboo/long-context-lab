import unittest

from long_context_lab.compression import compress
from long_context_lab.retrieval import rank_windows
from long_context_lab.planner import expand


class Tests(unittest.TestCase):
    def test_compression_budget(self):
        out=compress("alpha one. beta target two. gamma three.","target",30)
        self.assertLessEqual(len(out),30)
        self.assertIn("target",out)

    def test_retrieval(self):
        text="alpha "*50+"special target code "+"omega "*50
        parts=rank_windows(text,"target code",100,10,2)
        self.assertTrue(any("target" in x for x in parts))

    def test_plan(self):
        rows=expand({"target_tokens":[1000],"positions":[.5],"strategies":["full","retrieval"],"repeats":2})
        self.assertEqual(len(rows),4)


if __name__=="__main__":
    unittest.main()
