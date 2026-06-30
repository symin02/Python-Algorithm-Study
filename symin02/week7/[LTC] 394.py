class Solution:
    def decodeString(self, s: str) -> str:
        stack = []         # 이전 상태(문자열, 곱할 숫자)를 백업해둘 스택
        current_str = ""   # 현재 조립 중인 문자열
        current_num = 0    # 현재 계산 중인 반복 횟수
        
        for char in s:
            if char.isdigit():
                # 숫자가 두 자리 이상일 수 있으므로 자릿수를 올려가며 더함
                current_num = current_num * 10 + int(char)
                
            elif char == '[':
                # 여는 괄호를 만나면 새로운 패턴이 시작되므로 지금까지 만든 걸 스택에 백업
                stack.append((current_str, current_num))
                # 백업 뒤 현재 상태는 다시 초기화
                current_str = ""
                current_num = 0
                
            elif char == ']':
                # 닫는 괄호면 패턴 하나가 끝났으니 스택에서 이전 상태로 ㄱ
                prev_str, prev_num = stack.pop()
                # 이전 문자열에다가 (현재 괄호 안의 문자열 * 반복 횟수)를 붙여줌
                current_str = prev_str + (current_str * prev_num)
                
            else:
                # 일반 알파벳이면 현재 문자열에 계속 이어 붙임
                current_str += char
                
        return current_str