from typing import List

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = second = 2**31 - 1

        for num in nums:
            if num <= first:
                first = num     # num이 first보다 작다면 first에 num 대입
            elif num <= second:
                second = num    # num이 first보다 크지만 second보다 작다면 second에 num 대입
            else:
                return True     # num이 first, second보다 클 경우 -> first < second < num일 경우 true
            
        return False
    
s = Solution()

print(s.increasingTriplet([5,4,3,2,1]))