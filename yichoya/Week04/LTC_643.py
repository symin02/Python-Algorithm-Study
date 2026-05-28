from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        prefix = [0] * (n + 1)

        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        answer = float('-inf')
        for i in range(n - k + 1):
            cur_sum = prefix[i + k] - prefix[i]
            # print(cur_sum)
            answer = max(answer, cur_sum)

        return answer / k