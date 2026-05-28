from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero = 0

        for notZero in range(len(nums)):
            if nums[notZero] != 0 and nums[zero] == 0:
                nums[notZero], nums[zero] = nums[zero], nums[notZero]

            if nums[zero] != 0:
                zero += 1
        print(nums)


s = Solution()
s.moveZeroes([0,1,0,3,12])

            
