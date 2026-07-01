from collections import deque

class RecentCounter(object):

    def __init__(self):
        # 이전 ping()을 통해 저장한 t값들을 기억하기 위해 인스턴스 변수 사용
        self.tmp = deque()

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.tmp.append(t)
        while self.tmp and self.tmp[0] < t - 3000:
            self.tmp.popleft()
        return len(self.tmp)
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)