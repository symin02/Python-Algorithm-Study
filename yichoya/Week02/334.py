import math
from typing import List

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        INF = math.inf
        first, second = INF, INF

        for n in nums:
            # 가장 작은 값 갱신
            if n <= first:
                first = n
            # first < n <= second 인 경우
            elif n <= second:
                second = n
            # first < second < n 인 경우
            else:
                return True

        return False