class Solution:
    def removeStars(self, s: str) -> str:
        stack = []

        # 한 문자씩 확인
        for c in s:
            # 현재 문자가 *이면 앞 문자 제거
            if stack and c == "*":
                stack.pop()

                # *이 아니면 스택에 넣는다
            else:
                stack.append(c)
        
        return ''.join(stack)