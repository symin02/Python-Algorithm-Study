from collections import deque
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        queue = deque(senate)

        # 현재 남아 있는 각 의원 수
        r_cnt = senate.count('R')
        d_cnt = senate.count('D')

        # 앞으로 ban되어야 할 각 의원 수
        ban_r, ban_d = 0, 0

        # 둘 중 한 진영의 의원이 모두 사라질 때까지
        while r_cnt > 0 and d_cnt > 0:
            senator = queue.popleft()
            
            if senator == 'R':
                # Radiant 의원이 ban되어야 하는 상황이면 제거
                if ban_r > 0:
                    r_cnt -= 1
                    ban_r -= 1
                # ban되지 않았다면 Dire 의원 한 명을 ban할 기회를 얻고 다시 큐에 append
                else:
                    ban_d += 1
                    queue.append(senator)
            else:
                if ban_d > 0:
                    d_cnt -= 1
                    ban_d -= 1
                else:
                    ban_r += 1
                    queue.append(senator)

        return "Radiant" if r_cnt > 0 else "Dire"