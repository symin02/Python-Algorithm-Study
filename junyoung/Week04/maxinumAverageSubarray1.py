from typing import List
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)

        # 초기 합
        cur_sum = sum(nums[:k])
        max_sum = cur_sum

        # 슬라이딩 윈도우
        # s = 0
        # for e in range(k, n):
        #     cur_sum += nums[e] - nums[s]
        #     s += 1

        #     if cur_sum > max_sum:
        #         max_sum = cur_sum

        # 변수 하나만 사용해서 슬라이디 윈도우 구현
        for s in range(k, n):
            cur_sum += nums[s] - nums[s - k]

            if cur_sum > max_sum:
                max_sum = cur_sum

        return max_sum / k
    
s = Solution()
print(s.findMaxAverage([1,12,-5,-6,50,3], 4))