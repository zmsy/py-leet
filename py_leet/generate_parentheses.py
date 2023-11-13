from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        Given n pairs of parentheses, write a function to generate all
        combinations of well-formed parentheses.
        """
        output: List[str] = []

        def dfs(opens: int, closes: int, string: str) -> None:
            # base case, we're at the total length.
            if len(string) == n * 2:
                output.append(string)
                return

            if opens < n:
                dfs(opens + 1, closes, f"{string}(")

            if closes < opens:
                dfs(opens, closes + 1, f"{string})")

        dfs(0, 0, "")
        return output
