# Permutations

from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        visited = [False] * n

        def recur(tmp):
            if len(tmp) == n:
                ans.append(tmp[:])
                return

            for i in range(n):
                if visited[i]:
                    continue
                visited[i] = True
                tmp.append(nums[i])
                recur(tmp)
                tmp.pop()
                visited[i] = False

        recur([])
        return ans
