from typing import List

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max_cnt = 0        # 역대 최고 높이
        current_cnt = 0    # 현재 지점의 높이

        # 고도 변화량을 하나씩 보면서 현재 높이에 더해준다
        for i in range(len(gain)):
            current_cnt += gain[i]   # 변화량만큼 현재 높이를 갱신
            
            # 현재 높이가 역대 최고 높이보다 높다면 갱신
            max_cnt = max(max_cnt, current_cnt)
            
        return max_cnt
    
    #테스트~