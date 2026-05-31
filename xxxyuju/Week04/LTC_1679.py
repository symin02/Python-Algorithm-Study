from typing import List
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = 0
        right = len(nums) - 1
        cnt = 0

        while left < right:
            total = nums[left] + nums[right]
            # 두 값의 합이 k와 같다면 cnt 증가 후 포인터 이동
            if total == k:
                cnt += 1
                left += 1
                right -= 1

            # 합이 k보다 작다면 left 이동
            elif total < k:
                left += 1
            
            # 합이 k보다 크다면 right 이동
            else:
                right -= 1
        
        return cnt