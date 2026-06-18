from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        
        for a in asteroids:
            # 스택이 비어있거나, 양수(오) 소행성이면 ㄱㅊ으니까 일단 넣음!
            if not stack or a > 0:
                stack.append(a)
            else:
                # 음수(왼) 소행성이 날아왔을 때의 연쇄 충돌 처리
                # 스택 맨 위가 양수이고, 날아온 음수의 크기가 더 크면 스택 안의 작은 양수들을 계속 박살냄!
                while stack and stack[-1] > 0 and abs(stack[-1]) < abs(a):
                    stack.pop()
                
                # 작은 양수들을 없새고 
                if not stack or stack[-1] < 0:
                    # 스택이 비었거나, 스택 맨 위도 같은 음수면 ㄱ
                    stack.append(a)
                elif abs(stack[-1]) == abs(a):
                    # 크기가 똑같다면 동반 폭발
                    stack.pop()
                
        return stack