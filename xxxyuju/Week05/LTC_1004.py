from typing import List
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        max_cnt = 0     # 조건을 만족하는 최대 길이
        zeros_cnt = 0   # 현재 구간 안의 0 개수
        cnt = 0         # 현재 구간 안의 1 개수

        left = 0
        right = 0 

        while right < len(nums):
            # 오른쪽 값을 현재 구간에 포함
            if nums[right] == 0:
                zeros_cnt += 1
            else:
                cnt += 1
            
            # 0이 k개보다 많다면 왼쪽 값을 하나 뺀다
            if zeros_cnt > k:
                if nums[left] == 0:
                    zeros_cnt -= 1
                else:
                    cnt -= 1
                left += 1
            
            # 현재 구간 길이 = 1의 개수 + 0의 개수
            max_cnt = max(max_cnt, cnt + zeros_cnt)
            right += 1

        return max_cnt