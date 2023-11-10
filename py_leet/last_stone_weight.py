import heapq
from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]

        # python is a minheap, so we need to 
        heap = [s * -1 for s in stones]
        heapq.heapify(heap)

        while len(heap) >= 2:
            a = heapq.heappop(heap) * -1
            b = heapq.heappop(heap) * -1

            remain = abs(a - b)
            if remain:
                heapq.heappush(heap, remain * -1)
        
        return heap[0] * -1 if len(heap) == 1 else 0
