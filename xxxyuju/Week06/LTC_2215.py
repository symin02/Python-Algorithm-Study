from typing import List
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:

        # 중복 제거 
        nums1_set = set(nums1)
        nums2_set = set(nums2)

        res1 = [x for x in nums1_set if x not in nums2_set]     # nums1에는 있지만 num2에 없는 값
        res2 = [x for x in nums2_set if x not in nums1_set]     # nums1에는 있지만 num2에 없는 값

        return [res1, res2]