from typing import List

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid[0])

        # grid를 열 기준으로 저장
        cols = []
        for i in range(n):
            tmp = []
            for j in range(n):
                tmp.append(grid[j][i])
            cols.append(tmp)

        # grid의 각 행마다 cols를 탐색하면서 카운트
        ans = 0
        for i in range(n):
            for j in range(n):
                if grid[i] == cols[j]:
                    ans += 1

        return ans

