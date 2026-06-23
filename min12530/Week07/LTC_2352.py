from typing import List

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        count = 0
        
        for i in range(n):
            for j in range(n):
                
                row = grid[i]

                col = []
                for k in range(n):
                    col.append(grid[k][j])
                
                if row == col:
                    count += 1
                    
        return count