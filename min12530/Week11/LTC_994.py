from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        queue = deque()
        fresh_count = 0

        # 1. 모든 칸을 확인
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    # 썩은 오렌지를 큐에 저장
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    # 신선한 오렌지 개수 세기
                    fresh_count += 1

        # 처음부터 신선한 오렌지가 없다면 0분
        if fresh_count == 0:
            return 0

        directions = [
            (1, 0),   # 아래
            (-1, 0),  # 위
            (0, 1),   # 오른쪽
            (0, -1)   # 왼쪽
        ]

        minutes = 0

        # 2. BFS 시작
        while queue and fresh_count > 0:
            # 현재 시간대에 존재하는 썩은 오렌지 개수
            current_size = len(queue)

            # 1분 경과
            minutes += 1

            # 현재 썩은 오렌지들만 처리
            for _ in range(current_size):
                r, c = queue.popleft()

                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc

                    # 범위 안에 있고 신선한 오렌지인 경우
                    if (
                        0 <= nr < rows
                        and 0 <= nc < cols
                        and grid[nr][nc] == 1
                    ):
                        # 신선한 오렌지를 썩은 오렌지로 변경
                        grid[nr][nc] = 2

                        # 다음 시간에 주변을 썩게 할 오렌지
                        queue.append((nr, nc))

                        fresh_count -= 1

        # 3. 신선한 오렌지가 남았다면 불가능
        if fresh_count > 0:
            return -1

        return minutes