from typing import List
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        stack = []

        for x in asteroids:
            # 이전 소행성은 오른쪽으로 가고 현재 소행성은 왼쪽으로 가는 경우 충돌 발생
            while stack and x < 0 and stack[-1] > 0:

                # 스택의 소행성이 더 크면 현재 소행성 소멸 
                if abs(stack[-1]) > abs(x):
                    break

                # 현재 소행성이 더 크면 스택의 소행성 소멸
                elif abs(stack[-1]) < abs(x):
                    stack.pop()

                # 크기가 같으면 둘다 소멸
                else:
                    stack.pop()
                    break

            # 충돌 없이 살아남은 경우 스택에 넣는다
            else:
                stack.append(x)

        return stack