from typing import List
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        zero_cnt, zero, max_cnt = 0, 0, 0
        
        # 전체 배열 중 0이 아닌 숫자를 탐색하는 index(윈도우의 오른쪽 index)
        for not_zero in range(len(nums)):
            if not nums[not_zero]:
                zero_cnt += 1
            
            # zero: 0을 탐색하는 index(윈도우 왼쪽)
            while zero_cnt > k:
                # zero가 0을 가르키면 윈도우 왼쪽 증가 및 zero_cnt 감소
                if not nums[zero]:
                    zero_cnt -= 1
                zero += 1
            
            max_cnt = max(max_cnt, not_zero - zero + 1)

        return max_cnt
        
    
s = Solution()
print(s.longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3))