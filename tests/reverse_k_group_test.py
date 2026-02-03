import unittest
from py_leet.reverse_k_group import Solution
from py_leet import linked_list_from_array, array_from_linked_list


class TestReverseKGroups(unittest.TestCase):
    sol = Solution()

    def test1(self):
        input_list = [1, 2, 3, 4, 5]
        linked_list = linked_list_from_array(input_list)
        result = self.sol.reverseKGroup(linked_list, 2)
        result_list = array_from_linked_list(result)
        self.assertEqual(result_list, [2, 1, 4, 3, 5])

    def test2(self):
        input_list = [1, 2, 3, 4, 5]
        linked_list = linked_list_from_array(input_list)
        result = self.sol.reverseKGroup(linked_list, 3)
        result_list = array_from_linked_list(result)
        self.assertEqual(result_list, [3, 2, 1, 4, 5])
