from typing import List
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:

        n = len(grid)
        cols = []

        # 각 열을 하나씩 만든다
        for col in range(n):
            tmp = []
            for row in range(n):
                tmp.append(grid[row][col])
            cols.append(tmp)

        # 행과 열이 같은 경우의 개수를 센다
        return sum(row == col for row in grid for col in cols)