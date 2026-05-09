class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        count = 0
        
        for i in range(len(flowerbed)):
            if flowerbed[i]==0:

                # 왼쪽과 오른쪽이 비었는지 확인
                left = (i==0) or (flowerbed[i-1]==0)
                right = (i==len(flowerbed)-1) or (flowerbed[i+1]==0)

                # 왼쪽과 오른쪽이 0 이라면
                if left and right:
                    flowerbed[i]=1
                    count +=1

        return count >= n

