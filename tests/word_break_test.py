import unittest
from py_leet.word_break import Solution
from typing import List


class TestWordBreak(unittest.TestCase):
    def runOne(self, inp: str, words: List[str], out: bool):
        sol = Solution()
        self.assertEqual(sol.wordBreak(inp, words), out)

    def test1(self):
        self.runOne("leetcode", ["leet", "code"], True)

    def test2(self):
        self.runOne("applepenapple", ["apple", "pen"], True)

    def test3(self):
        self.runOne("catsandog", ["cats", "dog", "sand", "and", "cat"], False)
