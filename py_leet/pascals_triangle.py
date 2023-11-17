from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        output: List[List[int]] = []

        for i in range(numRows):
            row: List[int] = []
            for j in range(i):
                left = output[i - 1][j - 1] if j > 0 & i > 0 else 1
                right = output[i - 1][j] if i > 0 and j < i - 1 else 0
                row.append(left + right)

            output.append(row)

        return output
