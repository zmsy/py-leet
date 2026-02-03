from typing import List


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return 0

        i = 0
        j = len(arr) - 1
        while i < j:
            idx = (i + j) // 2
            idx2 = idx + 1
            if arr[idx] >= arr[idx2]:
                j = idx
            else:
                i = idx2

        return j
