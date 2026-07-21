class SmallestInfiniteSet:

    def __init__(self):
        # 1부터 1000까지의 set함수 생성
        # nums를 set으로 만들어 후에 값을 찾을 때 시간복잡도 O(n)로 찾기 가능
        self.nums = set(range(1, 1001))

    def popSmallest(self) -> int:
        min_num = min(self.nums)
        self.nums.remove(min_num)
        return min_num

    def addBack(self, num: int) -> None:
        self.nums.add(num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
