import unittest
from py_leet.decode_ways import Solution


class TestDecodeWays(unittest.TestCase):
    def test1(self):
        sol = Solution()
        self.assertEqual(sol.numDecodings("12"), 2)

    def test2(self):
        sol = Solution()
        self.assertEqual(sol.numDecodings("226"), 3)
