from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandies = max(candies)

        # extraCandies를 더했을 때 최댓값 이상이면 True
        return [x + extraCandies >= maxCandies for x in candies]