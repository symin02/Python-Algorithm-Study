from typing import List
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        
        # 원래 도로 방향 저장
        d = set()

        # graph에는 양방향으로 저장
        for a, b in connections:
            graph[a].append(b)
            graph[b].append(a)
            d.add((a, b))

        visited = [False] * n
        cnt = 0
        
        def dfs(node):
            nonlocal cnt
            visited[node] = True
            
            # 현재 도시와 연결된 도시 탐색
            for nxt in graph[node]:
                if not visited[nxt]:
                    # 0번 도시와 반대 방향인 도로라면 cnt 증가
                    if (node, nxt) in d:
                        cnt += 1
                    dfs(nxt)

        dfs(0)
        return cnt
