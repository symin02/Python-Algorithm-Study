from typing import List
import heapq
class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        # nums2 기준 내림차순 정렬
        nums_sort = list(zip(nums2, nums1))
        nums_sort.sort(reverse=True)

        # 선택한 nums1 값들을 저장할 최소 힙
        heap = []
        ans = 0
        sum_num1 = 0

        # 처음 k개 원소 선택
        for i in range(k):
            num2, num1 = nums_sort[i]
            heapq.heappush(heap, num1)
            sum_num1 += num1
        
        # 현재 nums2의 최솟값은 k번째 원소의 nums2
        ans = sum_num1 * nums_sort[k-1][0]

        # 이후 원소를 하나씩 추가
        for num2, num1 in nums_sort[k:]:
            heapq.heappush(heap, num1)
            sum_num1 += num1

            # k개만 유지하기 위해 가장 작은 nums1 제거
            min_num1 = heapq.heappop(heap)
            sum_num1 -= min_num1
            
            ans = max(ans, sum_num1 * num2)

        return ans
