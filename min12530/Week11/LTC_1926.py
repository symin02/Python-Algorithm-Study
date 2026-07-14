from collections import deque
from typing import List


class Solution:
    def nearestExit(
        self,
        maze: List[List[str]],
        entrance: List[int]
    ) -> int:

        m, n = len(maze), len(maze[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        r, c = entrance

        q = deque([(r, c, 0)])

        visited = [[False] * n for _ in range(m)]
        visited[r][c] = True

        while q:
            r, c, dist = q.popleft()

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if (
                    0 <= nr < m
                    and 0 <= nc < n
                    and maze[nr][nc] == '.'
                    and not visited[nr][nc]
                ):
                    # 다음 칸이 가장자리이면 출구
                    if (
                        nr == 0
                        or nr == m - 1
                        or nc == 0
                        or nc == n - 1
                    ):
                        return dist + 1

                    visited[nr][nc] = True
                    q.append((nr, nc, dist + 1))

        return -1