class Solution:
    def removeStars(self, s: str) -> str:
        stack = []  
        
       #문자열을 한 글자씩 탐색
        for char in s:
            if char == '*':
                # 별을 만나면 스택에서 가장 최근 글자를 하나 뻼
                stack.pop()
            else:
                # 일반 글자면 스택에 쌓아줌
                stack.append(char)
                
        # 남은 글자들이 담긴 리스트를 다시 하나의 문자열로 붙여서 리턴
        return "".join(stack)