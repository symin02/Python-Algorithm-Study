class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        max_window = 0
        num_zeros = 0
        left = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                num_zeros += 1
            while num_zeros > k:
                if nums[left] == 0:
                    num_zeros -= 1
                left += 1
            window = right - left + 1
            max_window = max(max_window, window)
        
        return max_window