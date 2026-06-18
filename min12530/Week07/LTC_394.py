def decodeString(s: str) -> str:
    stack = []
    current_str = ""
    current_num = 0
    
    for char in s:
        if char.isdigit():
            # 1. 숫자를 만났을 때: 두 자리 이상 숫자일 수 있으니 자릿수를 올려가며 더해줍니다.
            current_num = current_num * 10 + int(char)
            
        elif char == '[':
            # 2. 여는 괄호를 만났을 때: 현재까지의 문자열과 숫자를 스택에 '저장'하고 '초기화'합니다.
            stack.append((current_str, current_num))
            current_str = ""
            current_num = 0
            
        elif char == ']':
            # 3. 닫는 괄호를 만났을 때: 스택에서 마지막에 저장한 애들을 '꺼내서 조립'합니다.
            prev_str, repeat_times = stack.pop()
            current_str = prev_str + (current_str * repeat_times)
            
        else:
            # 4. 일반 알파벳을 만났을 때: 그냥 현재 문자열에 이어 붙입니다.
            current_str += char
            
    return current_str