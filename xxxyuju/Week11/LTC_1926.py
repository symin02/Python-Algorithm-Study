from collections import deque
from typing import List
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:

        q = deque()
        row_len, col_len = len(maze), len(maze[0])
        visited = [[False] * col_len for _ in range(row_len)]
        
        # entrance 방문 처리 후 거리 0으로 시작
        er, ec = entrance
        visited[er][ec] = True
        q.append((er, ec, 0))

        dr = [-1, 1, 0, 0]
        dc = [0, 0, -1, 1]

        while q:
            r, c, dist = q.popleft()

            # 상하좌우로 이동 가능한 칸 확인
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]

                if 0 <= nr < row_len and 0 <= nc < col_len:
                    if not visited[nr][nc] and maze[nr][nc] == ".":
                        # 가장자리에 도착하면 가장 가까운 출구
                        if nr == 0 or nr == row_len - 1 or nc == 0 or nc == col_len - 1:
                            return dist + 1
                        visited[nr][nc] = True
                        q.append((nr, nc, dist+1))

        
        return -1
                        

            
            

        