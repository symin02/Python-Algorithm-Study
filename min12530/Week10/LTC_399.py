from collections import defaultdict
from typing import List


class Solution:
    def calcEquation(
        self,
        equations: List[List[str]],
        values: List[float],
        queries: List[List[str]]
    ) -> List[float]:

        graph = defaultdict(list)

        # 그래프 생성
        for (a, b), value in zip(equations, values):
            graph[a].append((b, value))
            graph[b].append((a, 1 / value))

        def dfs(current, target, result, visited):
            # 목표 변수에 도착한 경우
            if current == target:
                return result

            visited.add(current)

            # 현재 변수와 연결된 변수 탐색
            for next_node, value in graph[current]:
                if next_node not in visited:
                    answer = dfs(
                        next_node,
                        target,
                        result * value,
                        visited
                    )

                    if answer != -1.0:
                        return answer

            return -1.0

        answers = []

        for start, end in queries:
            # 둘 중 하나라도 존재하지 않는 변수이면 계산 불가능
            if start not in graph or end not in graph:
                answers.append(-1.0)
            else:
                answers.append(dfs(start, end, 1.0, set()))

        return answers