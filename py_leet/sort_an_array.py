from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) >= 2:
            mid = len(nums) // 2
            left = nums[:mid]
            right = nums[mid:]
            left = self.sortArray(left)
            right = self.sortArray(right)
            return self.merge(left, right)

        return nums

    def merge(self, a: List[int], b: List[int]) -> List[int]:
        output: List[int] = []
        while len(a) and len(b):
            if a[0] <= b[0]:
                output.append(a.pop(0))
            else:
                output.append(b.pop(0))

        # add the rest of the lists if they exist
        output.extend(a)
        output.extend(b)
        return output
