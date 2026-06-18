class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []

        for ch in s:
            if ch != ']':
                stack.append(ch)
            else: 
                tmp = []    # 다음 루프에도 사용되므로 tmp 비우기
                while stack and stack[-1] !='[':
                    tmp.append(stack.pop())
                stack.pop() # stack에 남아 있는 '[' 제거 

                 # '[' 왼쪽에 숫자가 있다면 숫자만큼 반복, 아니면 1번만 반복
                num = []
                # isdigit():문자열 repeat가 숫자 문자열('3')이라면 true, 아니면 flase
                while stack and stack[-1].isdigit():
                    num.append(stack.pop())

                repeat = int(''.join(reversed(num)))    
                ans = ''.join(reversed(tmp)) * repeat

                for c in ans:
                    stack.append(c)
            
        return ''.join(stack)
    
s = Solution()
print(s.decodeString("3[a2[c]]"))