import unittest
from py_leet.odd_even_linked_list import Solution
from py_leet import linked_list_from_array, array_from_linked_list


class TestOddEvenLinkedList(unittest.TestCase):
    def test1(self):
        sol = Solution()
        testval = linked_list_from_array([1, 2, 3, 4, 5])
        result = sol.oddEvenList(testval)
        resultval = array_from_linked_list(result)
        self.assertEqual(resultval, [1, 3, 5, 2, 4])

    def test2(self):
        sol = Solution()
        testval = linked_list_from_array([2, 1, 3, 5, 6, 4, 7])
        result = sol.oddEvenList(testval)
        resultval = array_from_linked_list(result)
        self.assertEqual(resultval, [2, 3, 6, 7, 1, 5, 4])
