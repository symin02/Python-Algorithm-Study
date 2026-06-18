class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack = []

        stack.append(asteroids[0])
        for i in range(1, len(asteroids)):
            tmp = asteroids[i]      

            while stack and tmp < 0 and stack[-1] > 0:
                if abs(tmp) > abs(stack[-1]) and stack[-1] > 0: 
                    stack.pop()
                elif -tmp == stack[-1]:
                    stack.pop()
                    break
                else:
                    break
            else:
                stack.append(tmp)
               
        return stack
    
s = Solution()
print(s.asteroidCollision([3,5,-6,2,-1,4]))
        