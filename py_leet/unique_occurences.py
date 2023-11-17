from typing import List
from collections import Counter


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counts = Counter(arr)
        occurrences = Counter(counts.values())

        for occurrence in occurrences.values():
            if occurrence > 1:
                return False
        return True
