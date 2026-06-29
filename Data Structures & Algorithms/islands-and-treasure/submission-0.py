from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        r = len(grid)
        c = len(grid[0])

        q = deque()

        # Add all gates
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 0:
                    q.append((i, j))

        while q:
            i, j = q.popleft()

            for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if 0 <= x < r and 0 <= y < c and grid[x][y] == 2147483647:
                    grid[x][y] = grid[i][j] + 1
                    q.append((x, y))