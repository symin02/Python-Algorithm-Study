class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_length = 0
        num_zeros = 0
        left = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                num_zeros += 1
            while num_zeros > 1:
                if nums[left] == 0:
                    num_zeros -= 1
                left += 1
            
            max_length = max(max_length, right-left)
        return max_length