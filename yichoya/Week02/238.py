from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        nums = [1] + nums + [1]
        prefix = [1] * len(nums)
        suffix = [1] * len(nums)

        # nums[i] 기준 왼쪽 값들의 곱
        for i in range(1, len(nums) - 1):
            prefix[i] = prefix[i - 1] * nums[i - 1]

        # nums[i] 기준 오른쪽 값들의 곱
        for i in range(len(nums) - 2, 0, -1):
            suffix[i] = suffix[i + 1] * nums[i + 1]

        for i in range(1, len(nums) - 1):
            ans.append(prefix[i] * suffix[i])
        return ans



'''
2 <= nums.length <= 10^5

1, 2, 3, 4, 5
120, 60, 40, 30, 24

1, 2, 3, 4, 5, 0
0, 0, 0, 0, 0, 120
'''
