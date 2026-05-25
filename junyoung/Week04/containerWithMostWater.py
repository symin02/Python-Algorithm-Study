from typing import List 
class Solution:
    def maxArea(self, height: List[int]) -> int:
        # start= 0
        # end = len(height) - 1

        # # 첫 번째 물의 양(양 끝)
        # max_amount_water = (end - start) * min(height[start], height[end])
        # while start < end:
            
        #     # 높이가 더 낮은 쪽 포인터를 옮기기
        #     if height[start] < height[end]:
        #         start += 1
        #     else:
        #         end -= 1

        #     # 현재 물의 양이 최대값보다 크면 갱신
        #     if (end - start) * min(height[start], height[end]) > max_amount_water:
        #         max_amount_water = (end - start) * min(height[start], height[end])

        # return max_amount_water

        ###
        len_h = len(height)
        start = 0
        end = len_h - 1

        max_height = max(height)
        area = (end - start) * min(height[start], height[end])
        while start < end:
            if height[start] < height[end]:
                start += 1
            else:
                end -= 1
            
            area = max(area, (end - start) * min(height[start], height[end]))
            
            if area >= max_height * (end - start):
                return area
            
        return area

s = Solution()
print(s.maxArea([1,8,6,2,5,4,8,3,7]))