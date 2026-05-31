# Combinations

from typing import List
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []

        def recur(cur, start, tmp):
            if cur == k:
                ans.append(tmp[:])
                return

            for i in range(start, n + 1):
                tmp.append(i)
                recur(cur + 1, i + 1, tmp)
                tmp.pop()

        recur(0, 1, [])
        return ans
