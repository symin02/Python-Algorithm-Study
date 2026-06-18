from typing import List

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        row_counts = {}
        
        # 가로줄
        for row in grid:
            t_row = tuple(row)
            # get() 함수로 횟수 카운트
            row_counts[t_row] = row_counts.get(t_row, 0) + 1
            
        ans = 0
        
        # 세로줄
        for col in zip(*grid):
            #현재 뽑아낸 세로줄과 똑같이 생긴 가로줄이 딕셔너리에 몇 개 있는지 확인, 일치하는 개수만큼 정답에 누적~!~!
            ans += row_counts.get(col, 0)
            
        return ans