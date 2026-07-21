from collections import Counter
from typing import List
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        # 각 숫자가 몇 번 나왔는지
        counter = Counter(nums)

        # 숫자를 큰 순서대로 정렬
        counter_sort = sorted(counter, reverse=True)

        # 큰 숫자부터 등장 횟수만큼 k 감소
        for n in counter_sort:
            k -= counter[n]

            # k번째로 큰 숫자를 찾은 경우
            if k <= 0:
                return n


        # 힙 연습
        # heap = []

        # for n in nums:
        #     heapq.heappush(heap, n)

        #     # 힙에는 가장 큰 숫자 k개만 들어가도록
        #     if len(heap) > k:
        #         heapq.heappop(heap)

        # 힙의 최솟값이 k번째로 큰 숫자
        # return heap[0]