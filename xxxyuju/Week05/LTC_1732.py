from typing import List
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:

        max_ans = 0
        altitude = 0

        for x in gain:
            altitude += x                       # 현재 고도
            max_ans = max(max_ans, altitude)    # 최댓값 비교 후 갱신

        return max_ans