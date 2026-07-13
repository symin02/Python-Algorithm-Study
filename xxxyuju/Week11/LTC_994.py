from collections import deque
from typing import List
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        m = len(grid[0])
        n = len(grid)
        
        dr = [-1, 1, 0, 0]
        dc = [0, 0, -1, 1]

        q = deque()
        cnt = 0
        minutes = 0

        # 썩어있는 경우 큐에 append, 신선한 경우 cnt 증가
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    q.append((i, j, 0))
                elif grid[i][j] == 1:
                    cnt += 1

        while q and cnt > 0:
            r, c, time = q.popleft()
            
            # 현재 위치의 상하좌우 확인
            for k in range(4):
                nr = r + dr[k]
                nc = c + dc[k]

                # 신선한 오렌지라면 썩게 만든 후 큐에 append
                if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == 1:
                    cnt -= 1
                    grid[nr][nc] = 2
                    nt = time + 1
                    minutes = nt
                    q.append((nr, nc, nt))

        # 신선한 오렌지가 남아있는 경우 -1 return
        if cnt > 0:
            return -1

        return minutes
        