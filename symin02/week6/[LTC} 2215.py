from typing import List

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        
        set1 = set(nums1)
        set2 = set(nums2)
        
        # set1 중에서 set2에는 없는 숫자만 남김
        ans1 = list(set1 - set2)
        
        # set2 중에서 set1에는 없는 숫자만 남김
        ans2 = list(set2 - set1)
        
        # 두 개의 리스트를 하나로 합쳐서 리턴
        return [ans1, ans2]