from typing import List


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        left, right = 0, len(nums) - 1
        answer = 0

        nums.sort()

        while left < right:
            tmp = nums[left] + nums[right]
            if tmp == k:
                answer += 1
                left += 1
                right -= 1
            elif tmp < k:
                left += 1
            else:
                right -= 1

        return answer