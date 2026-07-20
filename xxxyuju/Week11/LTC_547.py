from typing import List
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        visited = [False] * len(isConnected)
        cnt = 0

        def dfs(node):
            # 현재 도시 방문 처리
            visited[node] = True
            
            # 연결되어 있는 도시들 중 아직 방문하지 않은 도시 탐색
            for nxt, connected in enumerate(isConnected[node]):
                if connected == 1 and not visited[nxt]:
                    dfs(nxt)

        # 방문하지 않은 도시가 발견되면 cnt 증가
        for x in range(len(isConnected)):
            if not visited[x]:
                cnt += 1
                dfs(x)

        return cnt
        