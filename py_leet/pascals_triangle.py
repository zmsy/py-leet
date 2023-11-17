from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []

        output: List[List[int]] = [[1]]

        for i in range(1, numRows):
            row: List[int] = []
            for j in range(i + 1):
                left = output[i - 1][j - 1] if j > 0 and i > 0 else 0
                right = output[i - 1][j] if i > 0 and j < i else 0
                row.append(max(left + right, 1))

            output.append(row)

        return output
