from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
            
        p = 0       # 0이 아닌 숫자가 들어갈 위치 
        zeros = nums.count(0)   # 뒤에 채워야 할 0의 개수

        # 순회하면서 0이 아닌 숫자만 앞쪽으로 이동
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[p] = nums[i]
                p += 1

        # p 이후의 위치는 모두 0으로 채운다
        nums[p:] = [0] * zeros