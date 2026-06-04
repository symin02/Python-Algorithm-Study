from collections import List
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0
        right = 0

        zeros_cnt = 0   # 현재 구간 안의 0 개수
        max_cnt = 0
        cnt = 0

        # 배열 안이 전부 1이면 길이 - 1 반환
        if nums.count(0) == 0:
            return len(nums) - 1

        while right < len(nums):
            # 오른쪽 값을 현재 구간에 포함
            if nums[right] == 0:
                zeros_cnt += 1
            
            else:
                cnt += 1
            
            # 0이 2개 이상이면 조간을 만족하지 못하므로 왼쪽 값을 뺀다
            if zeros_cnt > 1:
                if nums[left] == 0:
                    zeros_cnt -= 1
                else:
                    cnt -= 1
                left += 1
            
            # 길이는 1의 개수와 같다
            max_cnt = max(max_cnt, cnt)
            right += 1

        
        # for문으로 풀어보자 !
        # for right in range(len(nums)):
        #     if nums[right] == 0:
        #         zeros_cnt += 1
        #     else:
        #         cnt += 1

        #     if zeros_cnt > 1:
        #         if nums[left] == 0:
        #             zeros_cnt -= 1
        #         else:
        #             cnt -= 1
        #         left += 1
            
        #     max_cnt = max(max_cnt, cnt)

        
        return max_cnt