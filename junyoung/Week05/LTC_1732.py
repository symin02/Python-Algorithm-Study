from typing import List
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        # 누적합 배열의 첫번째 요소는 0으로 설정
        p_sum = [0 for _ in range(len(gain) + 1)]

        # 두 번째 index부터 누적합 저장
        for i in range(len(gain)):
            p_sum[i + 1] = gain[i] + p_sum[i]

        return max(p_sum)
    
s = Solution()

print(s.largestAltitude([0,-4,-7,-9,-10,-6,-3,-1]))