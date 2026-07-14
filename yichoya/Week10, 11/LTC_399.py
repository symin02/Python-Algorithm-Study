from collections import defaultdict
from typing import List

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        # 노드가 문자라서 list 대신 defaultdict로 생성
        graph = defaultdict(list)
        for (a, b), val in zip(equations, values):
            graph[a].append((b, val))
            graph[b].append((a, 1 / val))

        def dfs(cur, dest, total, visited):
            if cur == dest:
                return total

            visited[cur] = True
            for nxt, weight in graph[cur]:
                if nxt not in visited:
                    res = dfs(nxt, dest, total * weight, visited)
                    if res != -1.0:
                        return res

            return -1.0

        ans = []
        for start, end in queries:
            # 존재하지 않는 노드인 경우
            if start not in graph or end not in graph:
                ans.append(-1.0)
                continue

            visited = {}
            ans.append(dfs(start, end, 1.0, visited))

        return ans