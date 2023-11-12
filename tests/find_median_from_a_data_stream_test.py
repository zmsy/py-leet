import unittest
from py_leet.find_median_from_a_data_stream import MedianFinder


class TestMedianFinder(unittest.TestCase):
    def test1(self):
        finder = MedianFinder()
        finder.addNum(1)
        finder.addNum(2)
        self.assertEqual(finder.findMedian(), 1.5)
        finder.addNum(3)
        self.assertEqual(finder.findMedian(), 2.0)

    def test2(self):
        finder = MedianFinder()
        finder.addNum(-1)
        self.assertEqual(finder.findMedian(), -1.0)
        finder.addNum(-2)
        self.assertEqual(finder.findMedian(), -1.5)
        finder.addNum(-3)
        self.assertEqual(finder.findMedian(), -2.0)
        finder.addNum(-4)
        self.assertEqual(finder.findMedian(), -2.5)
        finder.addNum(-5)
        self.assertEqual(finder.findMedian(), -3.0)
