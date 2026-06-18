from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        n = len(asteroids)
        stack = []

        for i in range(n):
            num = asteroids[i]

            if num > 0:
                stack.append(num)
            else:
                while stack and stack[-1] > 0:
                    # 현재 숫자(음수)와 stack[-1] 절댓값 비교
                    if abs(stack[-1]) < abs(num):
                        stack.pop()
                        if not stack:
                            stack.append(num)
                            break
                    elif abs(stack[-1]) > abs(num):
                        break
                    else:
                        stack.pop()
                        break
                else:
                    stack.append(num)

        return stack