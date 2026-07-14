from collections import deque
from typing import List

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m = len(maze)
        n = len(maze[0])
        dxy = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        visited = [[False] * (n) for _ in range(m)]

        q = deque([(entrance[0], entrance[1], 0)])
        visited[entrance[0]][entrance[1]] = True

        def bfs():
            while q:
                x, y, path = q.popleft()

                if (x, y) != (entrance[0], entrance[1]):
                    if x == 0 or x == m - 1 or y == 0 or y == n - 1:
                        return path

                for i in range(4):
                    nx, ny = x + dxy[i][0], y + dxy[i][1]

                    if 0 <= nx < m and 0 <= ny < n:
                        if maze[nx][ny] == '.' and not visited[nx][ny]:
                            visited[nx][ny] = True
                            q.append((nx, ny, path + 1))

            return -1

        return bfs()
