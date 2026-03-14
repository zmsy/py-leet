from typing import List


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def evaluate(val: str):
            """
            Return a new version of the string with all of the backspaced chars
            removed.
            """
            stack: List[str] = []
            for char in val:
                if char == "#":
                    if len(stack):
                        stack.pop()
                else:
                    stack.append(char)
            return "".join(stack)

        s_out = evaluate(s)
        t_out = evaluate(t)

        return s_out == t_out
