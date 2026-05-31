from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        # 양 끝에 0 추가
        flowerbed = [0] + flowerbed + [0]
        cnt = 0

        # 1부터 len-2까지 순회
        for i in range(1, len(flowerbed)-1):

            # n개를 심을 수 있다면 바로 종료
            if cnt >= n:
                return True

            # 현재 위치와 양옆이 모두 0이면 꽃 심기 가능
            if flowerbed[i-1] == 0 and flowerbed[i] == 0 and flowerbed[i+1] == 0:
                cnt += 1
                flowerbed[i] = 1
        
        return cnt >= n