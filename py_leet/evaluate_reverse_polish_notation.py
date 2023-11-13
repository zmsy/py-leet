from typing import List, Set


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators: Set[str] = set(["*", "/", "-", "+"])
        stack: List[int] = []

        for token in tokens:
            if token in operators:
                operand_1 = stack.pop()
                operand_2 = stack.pop()
                result = int(eval(f"{operand_2} {token} {operand_1}"))
                stack.append(result)

            else:
                stack.append(int(token))

        return stack[0]
