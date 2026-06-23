class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        tmp = []

        for c in s:

            # 닫는 괄호가 나오면 괄호 안의 문자열을 꺼낸다
            if c == ']':

                # '['가 나올 때까지
                while stack[-1] != '[':
                    tmp.append(stack.pop())
                
                stack.pop()     # '[' 제거

                nums = []
                
                # '[' 앞에 있던 숫자를 꺼낸다
                while stack and stack[-1].isdigit():
                    nums.append(stack.pop())
                
                nums.reverse()

                stack.append(int(''.join(nums)) * ''.join(reversed(tmp)))
                tmp = []
            else:
                stack.append(c)
        
        return ''.join(stack)
        