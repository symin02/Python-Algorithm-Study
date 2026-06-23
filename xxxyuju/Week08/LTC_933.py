class RecentCounter:

    def __init__(self):
        # 요청 시간 리스트
        self.req = []

    def ping(self, t: int) -> int:
        # t 추가
        self.req.append(t)

        # [t-3000, t] 안에 있는 요청만 남긴다
        self.req = [time for time in self.req if time >= t - 3000]

        return len(self.req)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)