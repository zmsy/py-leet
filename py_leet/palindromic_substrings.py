class Solution:
    def countSubstrings(self, s: str) -> int:
        if len(s) < 2:
            return len(s)

        count = 0
        for i in range(len(s)):
            count += self._substringAt(s, i, i)
            count += self._substringAt(s, i, i + 1)

        return count

    def _substringAt(self, s: str, l: int, r: int) -> None:
        count = 0
        while l >= 0 and r < len(s):
            if s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
            else:
                break

        return count
