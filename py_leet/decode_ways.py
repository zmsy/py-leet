from typing import DefaultDict
from collections import defaultdict


class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        if n == 1:
            return 1 if s[0] != "0" else 0

        cache: DefaultDict[int, int] = defaultdict(int)
        cache[0] = 1
        cache[1] = 1 if 0 < int(s[0]) <= 9 else 0
        for i in range(2, n + 1):
            # indices are non-inclusive of upper bound
            one_digit = int(s[i - 1 : i])  # just the prior digit
            two_digits = int(s[i - 2 : i])  # two digits

            if 0 < one_digit <= 9:
                cache[i] += cache[i - 1]
            if 10 <= two_digits <= 26:
                cache[i] += cache[i - 2]

        return cache[n]
