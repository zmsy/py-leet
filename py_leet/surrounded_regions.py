from typing import List, Deque, Set, Tuple
from collections import deque

Coords = Tuple[int, int]
directions: List[Coords] = [(1, 0), (-1, 0), (0, 1), (0, -1)]


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return

        m = len(board)
        n = len(board[0])
        visited: Set[Coords] = set()
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O" and (i, j) not in visited:
                    queue: Deque[Coords] = deque([(i, j)])
                    isolated: bool = True
                    marked: Set[Coords] = set([(i, j)])  # keep track of *this* island
                    while queue:
                        qI, qJ = queue.popleft()

                        # check the current node for surroundedness
                        for dI, dJ in directions:
                            nI = qI + dI
                            nJ = qJ + dJ

                            if not isolated or nI < 0 or nI >= m or nJ < 0 or nJ >= n:
                                isolated = False
                                continue

                            if (
                                (nI, nJ) in visited  # all-up visited set
                                or (nI, nJ) in marked  # this visited set
                                or board[nI][nJ] == "X"
                            ):
                                continue

                            marked.add((nI, nJ))
                            queue.append((nI, nJ))

                    # iterate through the visited nodes and mark all of them x
                    if isolated:
                        for mI, mJ in marked:
                            board[mI][mJ] = "X"

                    # merge this visited list into the overall one
                    visited.update(marked)
