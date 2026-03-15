from typing import List, DefaultDict
from collections import defaultdict


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if len(s) < 1:
            return False

        # array keeping track of all of the spaces in a given string
        # DP occurs here
        # the spaces prior to the given spot is checked to see if the current
        # space is reachable
        places: DefaultDict[int, bool] = defaultdict()
        places[-1] = True

        # loop through all places in the string
        for i in range(len(s)):
            # if the prior space was not reachable, this is not reachable.
            if not places.get(i - 1):
                continue

            for word in wordDict:
                word_len = len(word)
                # first, check to see if it goes past the end of the stirng, and
                # continue if that's the case
                if i + word_len > len(s):
                    continue

                # check if the next _n_ chars are the word
                next_str = s[i : i + word_len]
                if next_str == word:
                    # mark the last place in this current word as true
                    places[(i + word_len) - 1] = True
                    # checking indices
                    # cur i = 0
                    # 0 1 2 3 4 5 6 7 8
                    # d o g a n d c a t
                    # word = "dog"
                    # word_len = 3
                    # i + 3 = index 3
                    # so we should mark "g" aka index 2 as reachable

        return places.get(len(s) - 1) or False
