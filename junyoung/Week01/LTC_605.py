from typing import List 

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        # 길이가 1일 경우 처리
        if len(flowerbed) == 1:
            return (flowerbed[0] == 0 and n <= 1 ) or (flowerbed[0] == 1 and n == 0 ) 

        pos = 1
        
        # 0번쨰, 1번째 index가 0일경우 참 (0, 0, ~)
        if flowerbed[pos-1] == 0 and flowerbed[pos] == 0:
            flowerbed[pos-1] = 1
            n -= 1

        while(pos < len(flowerbed) - 1):
            if flowerbed[pos - 1] == 0 and flowerbed[pos] == 0 and flowerbed[pos + 1] == 0:
                flowerbed[pos] = 1
                pos += 2
                n -= 1
            else:
                pos += 1
        
        # 마지막 -1과 마지막이 0일 경우 참(~, 0, 0)
        if flowerbed[-2] == 0 and flowerbed[-1] == 0:
            flowerbed[-1] = 1
            n -= 1

        return n <= 0
        
s = Solution()
flowerbed = [0,0,1,0,1]
n = 1
print(s.canPlaceFlowers(flowerbed, n))



