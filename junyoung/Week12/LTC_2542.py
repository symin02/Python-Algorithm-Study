import heapq
from typing import List

class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        # nums1, numss2를 zip으로 묶음(같은 인자값을 기준으로 해야 함)
        # nums2를 기준으로 내림차순
        pair = sorted(zip(nums2, nums1), reverse=True)

        heap = []
        total = 0
        ans = 0

        # nums2, nums1 동시에 전체 순회
        for n2, n1 in pair:
            heapq.heappush(heap, n1)
            total += n1

            # heap은 최소값은 확정으로 구할 수 있기 때문에 pop을 이용해 최소값 제거 
            # nums1에서 가장 큰 k개의 원소 유지 가능
            if len(heap) > k:
                total -= heapq.heappop(heap)

            # 이전까지의 최대값과 비교 및 갱신
            if len(heap) == k:
                ans = max(ans, total * n2)

        return ans
