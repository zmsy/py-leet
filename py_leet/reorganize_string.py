from typing import DefaultDict, List, Tuple
from collections import defaultdict
import heapq


class Solution:
    def reorganizeString(self, s: str) -> str:
        counts: DefaultDict[str, int] = defaultdict(int)
        for c in s:
            counts[c] += 1

        heap: List[Tuple[int, str]] = [(-y, x) for x, y in counts.items()]
        heapq.heapify(heap)

        output = ""
        while heap:
            [count, char] = heapq.heappop(heap)
            if not output or char != output[-1]:
                output += char
                count += 1
                if count:
                    heapq.heappush(heap, (count, char))
            # pop a different one and use that, and then add
            # the original one back
            else:
                if not heap:
                    return ""
                [count2, char2] = heapq.heappop(heap)
                output += char2
                count2 += 1
                if count2:
                    heapq.heappush(heap, (count2, char2))
                heapq.heappush(heap, (count, char))

        return output
