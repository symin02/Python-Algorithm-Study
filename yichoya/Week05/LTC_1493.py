from typing import List

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        start, end = 0, 0
        start = 0
        zero_cnt = 0
        ans = -12345

        while end < len(nums):
            if nums[end] == 0:
                zero_cnt += 1

            # zero 개수에 따라 시작점 이동 시키기
            while zero_cnt > 1:
                if nums[start] == 0:
                    zero_cnt -= 1
                start += 1

            ans = max(ans, end - start)
            end += 1

        return ans