class Solution:
    def maxArea(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1
        max_water = 0 # 역대 최고 물의 양을 저장할 바구니

        while left < right:
            # 1. 가로 길이 구하기
            width = right - left

            # 2. 세로 길이는 둘 중 '더 낮은 벽'의 높이
            current_height = min(height[left], height[right])

            # 3. 현재 면적 구해서 최고점(max_water) 갱신하기
            current_water = width * current_height
            max_water = max(max_water, current_water)

            # 4. [핵심 추론] 더 낮은 벽의 포인터를 이동시키기
            if height[left] < height[right]:
                left += 1
            else: 
                right -= 1

        return max_water
