from collections import defaultdict
from typing import List
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # 각 문자와 연결된 문자, 나눗셈 값을 저장
        graph = defaultdict(list)

        for (a, b), val in zip(equations, values):
            graph[a].append((b, val))   # a / b = val
            graph[b].append((a, 1.0/val))   # b / a = 1 / val

        ans = []

        def dfs(node, target, visited):
            # target 문자에 도착하면 1 반환
            if node == target:
                return 1.0
            
            visited.add(node)

            # 현재 문자와 연결된 문자 탐색
            for nxt, weight in graph[node]:
                if nxt not in visited:
                    res = dfs(nxt, target, visited)

                    # 목표에 도달했다면 경로의 값들을 곱해서 반환
                    if res != -1.0:
                        return weight * res

            # target까지 갈 수 없는 경우
            return -1.0

        for start, end in queries:
            # query에 등장하지 않은 문자가 포함된 경우
            if start not in graph or end not in graph:
                ans.append(-1.0)
            else:
                ans.append(dfs(start, end, set()))
            
        return ans