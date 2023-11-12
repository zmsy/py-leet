import heapq
from typing import List, Tuple


class MedianFinder:
    total: int
    left_heap: List[Tuple[int, int]]
    right_heap: List[Tuple[int, int]]

    def __init__(self):
        # keeps the smaller half of the array
        self.left_heap = []  # max heap
        self.right_heap = []  # min heap

    def addNum(self, num: int) -> None:
        heapq.heappush(self.left_heap, -1 * num)

        if (
            self.left_heap
            and self.right_heap
            and (-1 * self.left_heap[0]) > self.right_heap[0]
        ):
            val = -1 * heapq.heappop(self.left_heap)
            heapq.heappush(self.right_heap, val)

        # left heap should always be bigger or equal size
        if len(self.right_heap) < len(self.left_heap) - 1:
            val = -1 * heapq.heappop(self.left_heap)
            heapq.heappush(self.right_heap, val)
        if len(self.left_heap) < len(self.right_heap) - 1:
            val = -1 * heapq.heappop(self.right_heap)
            heapq.heappush(self.left_heap, val)

    def findMedian(self) -> float:
        total = len(self.left_heap) + len(self.right_heap)

        # odd case, return the larger lists min value
        if total % 2 != 0:
            if len(self.left_heap) > len(self.right_heap):
                return self.left_heap[0] * -1
            return self.right_heap[0]

        left_val = -1 * self.left_heap[0]
        right_val = self.right_heap[0]
        return (left_val + right_val) / 2.0
