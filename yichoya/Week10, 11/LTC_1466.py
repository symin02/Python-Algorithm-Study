from typing import List

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]  # 연결 그래프
        connections_set = set()
        # connections: 원래 연결 방향
        for a, b in connections:
            graph[a].append(b)
            graph[b].append(a)
            connections_set.add((a, b))

        visited = [False] * n
        res = 0

        def dfs(cur, visited):
            nonlocal res

            visited[cur] = True

            for nxt in graph[cur]:
                if not visited[nxt]:
                    # if [cur, nxt] in connections:
                    if (cur, nxt) in connections_set:
                        res += 1
                    dfs(nxt, visited)

        dfs(0, visited)
        return res
