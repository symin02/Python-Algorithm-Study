from collections import deque

class Solution:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        n = len(rooms)
        visited = set([0])
        queue = deque([0]) # 0번 방부터 탐색 시작
        
        while queue:
            current_room = queue.popleft()
                
                # 현재 방에서 얻은 열쇠 확인
            for key in rooms[current_room]:
                if key not in visited:
                        visited.add(key)
                        queue.append(key)
        
        # 방문한 방의 개수와 전체 방의 개수가 일치하는지 반환
        return len(visited) == n