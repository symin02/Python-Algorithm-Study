class Solution:
    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        def dfs(i):
            # 현재 도시 i를 방문 처리
            visited.add(i)
            # 도시 i와 연결된 다른 도시 j들을 탐색
            for j in range(n):
                if isConnected[i][j] == 1 and j not in visited:
                    dfs(j)
        
        n = len(isConnected)
        visited = set()
        provinces = 0
        
        # 모든 도시를 순회
        for i in range(n):
            if i not in visited:
                # 방문하지 않은 도시를 발견하면 새로운 주로 카운트
                provinces += 1
                dfs(i) # 해당 도시와 연결된 모든 도시를 방문 처리
                
        return provinces