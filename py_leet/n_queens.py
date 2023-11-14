from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        output: List[List[str]] = []

        # backtracking
        def backtrack(col: int, grid: List[List[str]]) -> None:
            nonlocal output
            # base case, we've reached the end.
            if col == n:
                joined = ["".join(x) for x in grid]
                output.append(joined)

            for i in range(n):  # rows
                if self.check_placement(grid, i, col):
                    # add a queen to the grid and continue backtracking
                    grid[i][col] = "Q"
                    # self._print_board(grid)
                    backtrack(col + 1, grid)
                    # remove so we can continue backtracking elsewhere
                    grid[i][col] = "."

        base_grid = [["."] * n for _ in range(n)]
        backtrack(0, base_grid)

        return output

    def check_placement(self, grid: List[List[str]], x: int, y: int) -> bool:
        m = len(grid)  # rows length
        n = len(grid[0])  # columns length
        # check same row
        for val in grid[x]:
            if val == "Q":
                return False

        # check same column
        for row in grid:
            if row[y] == "Q":
                return False

        # move to top left
        i, j = x, y
        while i >= 0 and j >= 0:
            if grid[i][j] == "Q":
                return False
            i -= 1
            j -= 1

        # move to top right
        i, j = x, y
        while i >= 0 and j <= n - 1:
            if grid[i][j] == "Q":
                return False
            i -= 1
            j += 1

        # move to bottom left
        i, j = x, y
        while i <= m - 1 and j >= 0:
            if grid[i][j] == "Q":
                return False
            i += 1
            j -= 1

        # move to bottom right
        i, j = x, y
        while i <= m - 1 and j <= n - 1:
            if grid[i][j] == "Q":
                return False
            i += 1
            j += 1

        return True

    def _print_board(self, grid: List[List[str]]) -> None:
        """
        Debug function to print out the entire board at any given point.
        """
        print("\n" + "\n".join(["".join(x) for x in grid]))
