from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        total = sum(nums)
        left = 0

        # left에 값을 누적하면서 오른쪽 구간의 합과 비교
        # right = total - left - nums[i]
        for i in range(n):
            if left == total - left - nums[i]:
                return i
            left += nums[i]

        return -1