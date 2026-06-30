from collections import deque

class RecentCounter:
    def __init__(self):
        self.queue = deque()

    def ping(self, t: int) -> int:
        self.queue.append(t) # 새로운 호출 시간 t가 들어오면 맨 뒤로 이동
       
        while self.queue and self.queue[0] < t - 3000: # 큐의 맨 앞인 가장 오래된 시간을 보면서, 유효시간이 지난 객체 버림
            self.queue.popleft() # 앞부터 지움
       
        return len(self.queue) # 정리후 남은 유효한 데이터들의 개수를 셈