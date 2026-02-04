from typing import Deque
from collections import deque


class HitCounter:
    def __init__(self):
        """
        Requirements:
            - Fast lookup of trailing 5 min

        Optimizations:
            - Low space utilization (don't keep everything around forever)
            - Able to optimize for duplicate timestamps

        Data structure: Queue/Array
        """
        self.q: Deque[int] = deque()

    def hit(self, timestamp: int) -> None:
        self.q.appendleft(timestamp)

    def getHits(self, timestamp: int) -> int:
        """
        Binary search for the index of the earliest timestamp that's >= time
        - 300s

        Then potentially trim the remainder
        """
        if len(self.q) == 0:
            return 0

        target = timestamp - 300

        # easy scenario: if the queue doesn't have any entries over 5 mins, just
        # return the length
        if target < self.q[-1]:
            return len(self.q)

        # otherwise binary search for the min timestamp, once this finishes the
        # 'lo' variable will be equal to the first timestamp that's higher than
        # the target timestamp, and we can return that index (or minus one, not
        # sure yet).
        lo = 0
        hi = len(self.q) - 1
        while lo < hi:
            # arrange in new -> old manner
            # [330, 320, 310, 300, 100, 90, 80, 70, 60, 50, 50, 40, 30, 20, 10]
            mid = (lo + hi) // 2
            val = self.q[mid]
            if val > target:
                lo = mid + 1
            else:
                hi = mid

        while len(self.q) > lo:
            self.q.pop()

        return lo
