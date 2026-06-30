from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        # 전체 길이를 n에 저장해 둡니다 (다음 라운드 진출 시 번호를 더해주기 위함)
        n = len(senate)
        
        # 각 팀의 순서를 담을 큐를 만듬
        r_queue = deque()
        d_queue = deque()
        
        # 각 팀원들이 서 있는 위치(인덱스)를 큐에 넣어줌
        for i, s in enumerate(senate):
            if s == 'R':
                r_queue.append(i)
            else:
                d_queue.append(i)
                
        #둘 중 한 팀의 큐가 완전히 빌 때까지 반복
        while r_queue and d_queue:
            r_idx = r_queue.popleft()
            d_idx = d_queue.popleft() # 맨 앞 뽑기
            
            # 더 앞번호인 사람이 먼저 공격해서 이김
            if r_idx < d_idx:
                # R win, go next round (원래 번호 + 전체 길이)
                r_queue.append(r_idx + n)
            else:
                # D win, go next round D
                d_queue.append(d_idx + n)
                
        #while문이 끝나면 살아남은 팀이 있는 거니까, 큐가 비어있지 않은 팀의 이름 띄우기
        return "Radiant" if r_queue else "Dire"

