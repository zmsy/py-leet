from collections import defaultdict
from typing import List, Tuple, DefaultDict


class TimeMap:
    cache: DefaultDict[str, List[Tuple[int, str]]]

    def __init__(self):
        self.cache = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.cache[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if not key in self.cache:
            return ""

        values = self.cache.get(key, [])
        l = 0
        r = len(values) - 1
        res = ""
        while l <= r:
            mid = (l + r) // 2
            if values[mid][0] <= timestamp:
                res = values[mid][1]
                l = mid + 1
            else:
                # don't assign result, because this isn't valid
                r = mid - 1

        return res
