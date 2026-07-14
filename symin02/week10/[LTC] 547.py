from typing import List

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = set()
        provinces = 0

        def dfs(cur_v):
            visited.add(cur_v)
            for v in range(n):
                # isConnected[cur_v][v] == 1 이면 직접 연결된 도시
                if isConnected[cur_v][v] == 1 and v not in visited:
                    dfs(v)
        
        for city in range(n):
            if city not in visited:
                dfs(city)
                provinces += 1   # 새로운 그룹을 발견할 때마다 +1

        return provinces