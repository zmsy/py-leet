from typing import List, Set


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        """
        The goal here is to use a stack in order to determine where parens are
        that can be removed.
        """
        to_remove: Set[int] = set()
        stack: List[int] = []
        for i, c in enumerate(s):
            if c == "(":
                stack.append(i)
            elif c == ")":
                if stack and s[stack[-1]] == "(":
                    stack.pop()
                else:
                    to_remove.add(i)

        # loop through and add any remaining open parens to the to_remove set
        for idx in stack:
            to_remove.add(idx)

        joined = "".join([c for i, c in enumerate(s) if i not in to_remove])
        return joined
