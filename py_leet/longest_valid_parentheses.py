class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # we need at least one open and close
        if len(s) < 2:
            return 0

        # keep track of the best we've seen so far
        best = 0

        # loop until the pointer finishes
        i = 0
        while i < len(s):
            # loop through until we find an open parenthesis
            while i < len(s) and s[i] != "(":
                i += 1

            if i == len(s):
                break

            # once we've found an open parentheses, start checking for valid parens
            # by using a stack.
            # optimization: this is not technically necessary, because the only
            # values stored in it are ["(", "("]. can use an int
            opens = 0  # prepopulate the first paren
            j = i
            inner_best = 0
            while j < len(s):
                if s[j] == ")":
                    # handle the close case
                    if opens == 0:  # nothing to compare w? break because we can't
                        break
                    else:
                        opens -= 1

                else:
                    # handle the open case - aka add to the stack and keep on
                    # moving
                    opens += 1

                # print(
                #     f"i = {i}, j = {j}, substr = {s[i : max(j + 1, len(s) - 1)]}, stack = {stack}"
                # )
                # if the stack is empty, record the length and compare with
                # the current best
                if opens == 0:
                    cur_best = j - i + 1
                    # print(f"updating best = {best}, {cur_best}")
                    inner_best = max(inner_best, cur_best)
                    best = max(best, cur_best)

                j += 1

            # if we reach the end and the stack still exists, it means that we
            # should keep iterating
            i += max(1, inner_best)

        return best
