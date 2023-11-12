import heapq
from math import sqrt
from typing import List, Tuple


class Solution:
    heap: List[Tuple[float, int]]

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        self.heap = []
        for point in points:
            # since python is by default a min-heap, we multiple these by -1 to keep smaller numbers closer
            distance = self._distance(point, [0, 0]) * -1
            if len(self.heap) < k:
                heapq.heappush(self.heap, (distance, point))
            else:
                heapq.heappushpop(self.heap, (distance, point))

        return [x[1] for x in self.heap]

    def _distance(self, a: List[int], b: List[int]) -> float:
        return abs(sqrt((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2))
