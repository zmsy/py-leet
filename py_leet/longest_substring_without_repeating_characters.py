from typing import Dict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)

        best = 0
        seen: Dict[str, int] = {}
        left = 0  # left pointer = l

        for right in range(0, len(s)):  # right pointer = r
            char = s[right]
            if char in seen and left <= seen[char]:
                # bring up the back
                left = seen[char] + 1

            seen[char] = right
            best = max(best, right - left)

        return best + 1
