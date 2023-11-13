import heapq
from typing import List, Sequence, DefaultDict, Tuple, Deque
from collections import defaultdict, deque


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts: DefaultDict[str, int] = defaultdict(int)
        for task in tasks:
            counts[task] += 1

        heap: Sequence[int] = [count * -1 for count in counts.values()]
        heapq.heapify(heap)
        queue: Deque[Tuple[int, int]] = deque()

        time = 0
        while queue or heap:
            time += 1

            if heap:
                val = heapq.heappop(heap)
                remaining = val + 1
                if remaining != 0:
                    queue.append((remaining, time + n))

            if queue and queue[0][1] == time:
                val = queue.popleft()
                heapq.heappush(heap, val[0])

        return time
