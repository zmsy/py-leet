from collections import defaultdict
from typing import DefaultDict


class Solution:
    """
    Naive solution - O(n * log n)
    """

    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1len = len(s1)
        s2len = len(s2)
        if s1len == 0 or s2len == 0:
            return False
        if s2len < s1len:
            return False
        if s2len == s1len:
            return sorted(s2) == sorted(s1)

        # count of all letters and their relative amounts
        counts: DefaultDict[str, int] = defaultdict(int)
        for letter in s1:
            counts[letter] += 1

        # populate for the first string portion
        for i in range(0, s1len - 1):
            letter = s2[i]
            if letter in counts:
                counts[letter] -= 1

        # iterate through the string, decrementing the count of each letter
        # found so far
        for right in range(s1len - 1, s2len):
            # calculate left bound and remove
            left = (right - s1len) + 1

            # take new letter as input
            letter = s2[right]
            if letter in counts:
                counts[letter] -= 1

            # check for correctness
            # could be sped up by keeping a total, but first version won't
            has_non_zero = False
            for value in counts.values():
                if value != 0:
                    has_non_zero = True
                    break

            if not has_non_zero:
                return True

            # remove the last letter as we move forward
            left_letter = s2[left]
            if left_letter in counts:
                counts[left_letter] += 1

        return False
