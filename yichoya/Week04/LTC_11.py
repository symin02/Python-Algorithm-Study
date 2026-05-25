from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        answer = -12345

        while left < right:
            # 현재 위치에서 담을 수 있는 물의 양 계산
            width = right - left
            water = width * min(height[left], height[right])
            answer = max(answer, water)

            # 선택된 두 막대 중 길이가 짧은 막대를 선택한 인덱스 이동
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return answer