import unittest
from py_leet.task_scheduler import Solution


class TestLeastInterval(unittest.TestCase):
    def test_least_interval_example1(self):
        tasks = ["A", "A", "A", "B", "B", "B"]
        n = 2
        expected = 8
        sol = Solution()
        result = sol.leastInterval(tasks, n)
        self.assertEqual(result, expected)

    def test_least_interval_example2(self):
        tasks = ["A", "A", "A", "B", "B", "B"]
        n = 0
        expected = 6
        sol = Solution()
        result = sol.leastInterval(tasks, n)
        self.assertEqual(result, expected)

    def test_least_interval_example3(self):
        tasks = ["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"]
        n = 2
        expected = 16
        sol = Solution()
        result = sol.leastInterval(tasks, n)
        self.assertEqual(result, expected)
