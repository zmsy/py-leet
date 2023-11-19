from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        parent_row: List[int] = [1]

        for i in range(1, rowIndex + 1):
            row: List[int] = []
            for j in range(i + 1):
                left = parent_row[j - 1] if j > 0 and i > 0 else 0
                right = parent_row[j] if i > 0 and j < i else 0
                row.append(max(left + right, 1))

            parent_row = row

        return parent_row
