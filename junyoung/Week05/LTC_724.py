from typing import List
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        # 배열 앞부터 누적합
        pre_sum = [0 for _ in range(n + 1)] 

        # 배열 뒤부터 누적합
        suf_sum = [0 for _ in range(n + 1)]

        for i in range(n):
            pre_sum[i + 1] = pre_sum[i] + nums[i]
            suf_sum[n - (i + 1)] = suf_sum[n - i] + nums[n - (i + 1)]

        for i in range(n):
            if pre_sum[i] == suf_sum[i + 1]:
                return i
        return -1
    
s = Solution()
print(s.pivotIndex([1,7,3,6,5,6]))