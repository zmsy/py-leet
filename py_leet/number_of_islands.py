from typing import List, Set, Tuple


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid) == 0:
            return 0

        if len(grid[0]) == 0:
            return 0

        # keep track of any spaces that were evaluated
        rows = len(grid)
        cols = len(grid[0])
        seen: Set[Tuple[int, int]] = set()
        islands = 0

        def bfs(i: int, j: int) -> None:
            queue: List[Tuple[int, int]] = [(i, j)]
            seen.add((i, j))
            while queue:
                node = queue.pop(0)
                neighbs = neighbors(*node)
                for neighb in neighbs:
                    seen.add(neighb)
                    i, j = neighb
                    if grid[i][j] == "1":
                        queue.append(neighb)

        def neighbors(i: int, j: int) -> List[Tuple[int, int]]:
            neighbs = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
            return [
                x
                for x in neighbs
                if x[0] >= 0
                and x[1] >= 0
                and x[0] < rows
                and x[1] < cols
                and x not in seen
            ]

        # traverse through rows
        for i in range(len(grid)):
            # traverse through columns
            for j in range(len(grid[0])):
                if (i, j) in seen:
                    continue

                char = grid[i][j]
                if char == "1":
                    islands += 1
                    bfs(i, j)

        return islands
