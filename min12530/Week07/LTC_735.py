class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
            n = len(asteroids)
            stack = []

            for a in asteroids:
                alive = True

                # 충돌할 경우
                while stack and a < 0 and stack[-1] > 0:
                    if a + stack[-1] > 0 :
                        alive = False
                        break
                    elif a + stack[-1] < 0:
                        stack.pop()
                        alive = True
                    else:
                        stack.pop()
                        alive = False
                        break
                if alive:
                    stack.append(a)

            return stack