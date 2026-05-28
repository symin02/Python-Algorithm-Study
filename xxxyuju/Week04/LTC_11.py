from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:
            # 넓이 구하기
            area = (right - left) * min(height[left], height[right])
            # print(left, right, area)
            if max_area < area:
                max_area = area

            # 높이가 더 낮은 쪽의 포인터 이동
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area