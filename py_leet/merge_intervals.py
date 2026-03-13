from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) < 2:
            return intervals

        intervals.sort(key=lambda x: x[0])
        i = 0
        while i < len(intervals) - 1:
            first = intervals[i]
            second = intervals[i + 1]

            # check to see if they're overlapping
            if first[1] >= second[0]:
                new = [min(first[0], second[0]), max(first[1], second[1])]
                intervals[i] = new
                intervals.pop(i + 1)
            else:
                i += 1

        return intervals
