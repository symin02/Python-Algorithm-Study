import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # # nums 정렬
        # nums.sort()

        # # 오름차순 정렬이므로 k번째로 큰 인덱스는 len(nums)에서 k만큼 뺀 값을 반환
        # return nums[len(nums) - k]



        ##### heap 이용한 풀이 #####
        # heap = []
        # # nums의 모든 원소를 heap에 넣기
        # for num in nums:
        #     heapq.heappush(heap, num)

        # # k번째 큰 수를 구하는 것이므로 (전체 길이 - k) 만큼 heappop() 해 최소값 제거
        # for _ in range(len(nums) - k):
        #     heapq.heappop(heap)
        
        # # heap의 0번째 인덱스에는 k번째 큰 수가 남아있음 
        # return heap[0]
        ### 위 방법은 전체 배열을 heap에 넣고 거기서 heap을 순회하는 방식이므로 ###
        ### 시간복잡도 nlogn -> sort()와 같음 ###


        ##### heap의 길이를 k로 고정시킨 풀이 #####
        heap = []
        for num in nums:
            heapq.heappush(heap, num)

            if len(heap) > k:
                heapq.heappop(heap)

        return heap[0]

