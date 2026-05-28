class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        count=0
        for i, x in enumerate(nums):
            if x!=0:
                nums.pop(i)
                nums.insert(count,x)
                count+=1
        