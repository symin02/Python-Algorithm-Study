from typing import List

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_cnt = 0      # 조건을 만족하는 최대 길이
        zeros_cnt = 0    # 현재 구간 안의 0 개수
        cnt = 0          # 현재 구간 안의 1 개수

        left = 0
        
        # 오른쪽 값을 하나씩 현재 구간에 포함시킨닼
        for right in range(len(nums)):
            if nums[right] == 0:
                zeros_cnt += 1
            else:
                cnt += 1
            
            # 0이 1개보다 많다면, 만족할 때까지 계속 왼쪽 값을 뺀다
            while zeros_cnt > 1:
                if nums[left] == 0:
                    zeros_cnt -= 1
                else:
                    cnt -= 1
                left += 1     # 왼쪽 손가락을 오른쪽으로 한 칸 당김
            
            # 현재 구간 안의 진짜 1의 개수로 최댓값 갱신
            max_cnt = max(max_cnt, cnt)

        if max_cnt == len(nums):
            return max_cnt - 1
            
        return max_cnt