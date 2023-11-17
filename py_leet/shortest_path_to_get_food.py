from typing import List, Tuple, Deque, Set
from collections import deque

Coords = Tuple[int, int]
directions: List[Coords] = [(1, 0), (-1, 0), (0, 1), (0, -1)]


class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return -1

        m = len(grid)
        n = len(grid[0])

        # find the starting point
        queue: Deque[Tuple[int, int, int]] = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "*":
                    queue.append((i, j, 0))
                    break

        visited: Set[Tuple[int, int]] = set()
        while queue:
            [cI, cJ, distance] = queue.popleft()
            if grid[cI][cJ] == "#":
                return distance
            visited.add((cI, cJ))

            for nI, nJ in [(cI + _i, cJ + _j) for _i, _j in directions]:
                if 0 <= nI < m and 0 <= nJ < n and not (nI, nJ) in visited:
                    queue.append((nI, nJ, distance + 1))

        return -1
