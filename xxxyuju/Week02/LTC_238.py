from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:  
        # n = len(nums)
        # prefix = [1] * n
        # suffix = [1] * n
        # res = [1] * n

        # for i in range(1, n):
        #     prefix[i] = prefix[i-1] * nums[i-1]
        #     suffix[n-i-1] = suffix[n-i] * nums[n-i]


        # 최종 풀이

        n = len(nums)
        res = [1] * n
        left = 1    # 왼쪽에서부터 누적한 곱
        right = 1   # 오른쪽에서부터 누적한 곱

        # left는 앞에서부터, right는 뒤에서부터 누적하며 한 번에 처리
        for i in range(n):
            # i 위치에는 왼쪽 곱을 반영
            res[i] *= left

            # n-i-1 위치에는 오른쪽 곱을 반영
            res[n-i-1] *= right

            # 다음 위치를 위해 현재 값 누적
            left *= nums[i]
            right *= nums[n-i-1]

        return res