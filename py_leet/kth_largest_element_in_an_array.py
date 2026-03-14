import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        Given an integer array nums and an integer k, return the kth largest element in the array.
        Note that it is the kth largest element in the sorted order, not the kth distinct element.
        Can you solve it without sorting?
        """
        vals = nums[:k]
        heapq.heapify(vals)
        for num in nums[k:]:
            if num > vals[0]:
                heapq.heappushpop(vals, num)

        return vals[0]
