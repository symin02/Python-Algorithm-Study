from typing import List

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [False] * (n + 1)

        # isConnected: 1이면 연결, 0이면 연결x
        def dfs(cur):
            visited[cur] = True
            for nxt in range(n):
                if isConnected[cur][nxt] == 1 and not visited[nxt]:
                    dfs(nxt)

        answer = 0
        for i in range(n):
            if not visited[i]:
                answer += 1
                dfs(i)

        return answer
