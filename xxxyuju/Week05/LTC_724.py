from typing import List
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        left_sum = [0] * n      # 각 위치 기준 왼쪽 합
        right_sum = [0] * n     # 각 위치 기준 오른쪽 합

        for i in range(1, n):
            # 앞에서부터 i번째 위치의 왼쪽 합 계산
            left_sum[i] = left_sum[i-1] + nums[i-1]

            # 뒤에서부터 오른쪽 합 계산
            right_sum[n-i-1] = right_sum[n-i] + nums[n-i] 

        # print(left_sum)
        # print(right_sum)

        for j in range(n):
            # 왼쪽 합과 오른쪽 합이 같으면 pivot index
            if left_sum[j] == right_sum[j]:
                return j

        return -1
        