from typing import List

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # triplet[0]: 증가 수열의 첫 번째 값 후보
        # triplet[1]: 증가 수열의 두 번째 값 후보
        triplet = [float('inf'), float('inf')]

        for n in nums:
            if n <= triplet[0]:
                triplet[0] = n
            elif n <= triplet[1]:
                triplet[1] = n
            else:
                # n이 두 번째 후보보다 크면 triplet[0] < triplet[1] < n 완성
                return True
        
        return False