class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row_dict = {}
        col_dict = {}
        cnt = 0

        # column dictionary 생성
        for c in range(len(grid[0])):
            col_dict[c] = []

        for r in range(len(grid)):
            row_dict[r] = grid[r]
            for c in range(len(grid[0])):
                col_dict[c].append(grid[r][c])

        for r in row_dict:
            for c in col_dict:
                if row_dict[r] == col_dict[c]:
                    cnt += 1
        return cnt

s = Solution()
c = s.equalPairs([[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]])
print(c)