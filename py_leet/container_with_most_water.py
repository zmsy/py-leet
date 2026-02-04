from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        Start with two pointers
        Until they meet, keep calculating the best volume and return it
        """
        if len(height) < 2:
            return 0

        lo = 0
        hi = len(height) - 1
        vol = 0
        while lo < hi:
            # calculate height
            y_axis = min(height[lo], height[hi])
            # calculate width
            x_axis = hi - lo
            # determine best volume
            vol = max(vol, y_axis * x_axis)
            if height[lo] > height[hi]:
                hi -= 1
            else:
                lo += 1

        return vol
