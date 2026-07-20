from typing import List


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]

        for a, b in connections:
            # 원래 방향 a -> b
            graph[a].append((b, 1))

            # 반대 방향으로 탐색할 수 있도록 추가
            graph[b].append((a, 0))

        visited = [False] * n

        def dfs(city):
            visited[city] = True
            count = 0

            for next_city, need_change in graph[city]:
                if not visited[next_city]:
                    count += need_change
                    count += dfs(next_city)

            return count

        return dfs(0)