from typing import List
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        # 초기 합
        tmp_sum = sum(nums[:k])

        left = 1
        right = k

        max_sum = tmp_sum

        # right가 배열 범위 안에 있을 동안 윈도우를 한 칸씩 이동
        while right < len(nums):

            # 이전 윈도우의 가장 왼쪽 값을 빼주고 새로 들어오는 값 저장
            tmp_sum -= nums[left-1]
            tmp_sum += nums[right]
            
            # 최대 값 비교 후 포인터 이동
            max_sum = max(max_sum, tmp_sum)
            left += 1
            right += 1

        # 최대 합을 k로 나누어 최대 평균 반환
        return max_sum / k