import heapq
class SmallestInfiniteSet:

    def __init__(self):
        # 다시 추가된 숫자들 저장
        self.heap = []

        # 아직 한 번도 안 꺼낸 가장 작은 숫자
        self.min_num = 1

    def popSmallest(self) -> int:
        # 다시 추가된 숫자가 있다면 그중 최솟값 반환
        if self.heap:
            return heapq.heappop(self.heap)

        # 힙이 비어있을 경우 새로운 숫자를 순서대로 return
        n = self.min_num
        self.min_num += 1
        return n
        

    def addBack(self, num: int) -> None:
        # 이미 꺼낸 숫자이고, 힙에 중복으로 들어있지 않은 경우에만 추가
        if num < self.min_num and num not in self.heap:
            heapq.heappush(self.heap, num) 
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)