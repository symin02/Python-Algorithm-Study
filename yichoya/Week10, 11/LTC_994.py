from typing import List
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dxy = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def bfs():
            ans = 0
            while q:
                x, y, time = q.popleft()
                ans = time

                for i in range(4):
                    nx, ny = x + dxy[i][0], y + dxy[i][1]

                    if 0 <= nx < m and 0 <= ny < n:
                        if grid[nx][ny] == 1:
                            grid[nx][ny] = 2
                            q.append((nx, ny, time + 1))

            return ans

        q = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i, j, 0))

        res = bfs()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1

        return res