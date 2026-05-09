from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        # is_gratest_arr = []
        # gratest_candies = max(candies)
        
        # for i in candies:
        #     if(i + extraCandies >= gratest_candies):
        #         is_gratest_arr.append(True)
        #     else:
        #         is_gratest_arr.append(False)

        # return is_gratest_arr

        # List Comprehension(반복 + 조건)을 이용해 한 줄로 작성
        gratest_candies = max(candies)
        return [c + extraCandies >= gratest_candies  for c in candies]

s= Solution()
candies = [2,3,5,1,3]
extraCandies = 3
print(s.kidsWithCandies(candies, extraCandies))
