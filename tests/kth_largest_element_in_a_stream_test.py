import unittest
from py_leet.kth_largest_element_in_a_stream import KthLargest

class TestKthLargest(unittest.TestCase):
    """
    https://leetcode.com/problems/kth-largest-element-in-a-stream/
    """

    def test1(self):
        kth = KthLargest(1, [])
        kth.add(-3)
        kth.add(-2)
        kth.add(-4)
        kth.add(0)
        kth.add(4)
