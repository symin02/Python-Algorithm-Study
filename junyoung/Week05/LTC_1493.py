from typing import List
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_cnt, zero_cnt, s = 0, 0, 0

        # nums에 1만 있을 경우
        if 0 not in nums:
            return len(nums) - 1
        
        # nums에 0만 있을 경우
        if 1 not in nums:
            return 0

        # 윈도우의 끝자리 e는 nums 완전 탐색
        for e in range(len(nums)):
            if nums[e] == 0:
                zero_cnt += 1

            # 윈도우에 포함된 0의 개수가 1 이상이면
            # 윈도우 시작점 s가 0 다음을 가리킬때까지 루프
            while zero_cnt > 1:
                if nums[s] == 0:
                    zero_cnt -= 1
                s += 1

            max_cnt = max(max_cnt, e - s + 1)

        return max_cnt - 1   

        
    
s = Solution()
print(s.longestSubarray([0,1,1,1,0,1,1,0,1]))