from typing import List

# [1,2,3,4]
# pre 배열에는 기준 index의 왼쪽의 누적곱
# index가 0일 경우 1, 1일 경우 1 * 1, 2일 경우 1 * 1 * 2, 3일 경우 1 * 1 * 2 * 3 
# pre = [1, 1, 2, 6]

# suf 배열에는 기준 index의 오른쪽의 누적곱
# index가 3일 경우 1, 2일 경우 1 * 4, 1일 경우 1 * 4 * 3, 0일 경우 1 * 4 * 3 * 2
# suf = [24, 12, 4, 1]

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre, suf, res = [1], [1], []
        pre_mul, suf_mul = 1, 1

        i, j = 1, 1
        for i in range(0, len(nums) - 1):
            pre_mul *= nums[i]
            pre.append(pre_mul)
        
        for j in range(len(nums) - 1, 0, -1):
            suf_mul *= nums[j]
            suf.append(suf_mul)

        suf.reverse()
        
        for i in range(len(nums)):
            res.append(pre[i] * suf[i])

        return res

s = Solution()
print(s.productExceptSelf([1,2,3,4]))      
        