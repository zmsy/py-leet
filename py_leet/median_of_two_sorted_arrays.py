from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        small, big = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2
        # use the smaller of the two arrays to search.
        if len(small) > len(big):
            small, big = big, small

        l = 0
        r = len(small) - 1
        while True:
            i = (l + r) // 2        # small middle point
            j = half - (i + 1) - 1  # large middle point

            small_left = small[i] if i >= 0 else float('-infinity')
            small_right = small[i + 1] if i < len(small) - 1 else float('infinity')
            big_left = big[j] if j >= 0 else float('-infinity')
            big_right = big[j + 1] if j < len(big) - 1 else float('infinity')

            # the condition we're checking for here is that the max of both left
            # partitions is smaller than the min of both right partitions.
            if small_left <= big_right and big_left <= small_right:
                # odd case
                if total % 2 == 1:
                    return min(small_right, big_right)
                # even case
                return (max(big_left, small_left) + min(small_right, big_right)) / 2
            
            elif small_left > big_right:
                r = i - 1
            else:
                l = i + 1
