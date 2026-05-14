class Solution:
    def compress(self, chars: list[str]) -> int:
        read = 0   # 문자를 읽어들이는 포인터
        write = 0  # 문자와 숫자를 기록하는 포인터
        n = len(chars)
        
        while read < n:
            current_char = chars[read]
            count = 0
            
            # 1. 연속된 동일한 문자의 개수를 세기
            while read < n and chars[read] == current_char:
                read += 1
                count += 1
                
            # 2. 문자를 기록 포인터 위치에 덮어쓰기
            chars[write] = current_char
            write += 1
            
            # 3. 개수가 1보다 크다면 숫자도 이어서 기록
            if count > 1:
                # 숫자가 10 이상일 수 있으므로 문자열로 변환 후 한 글자씩 기록
                for digit in str(count):
                    chars[write] = digit
                    write += 1
                    
        # write 포인터의 위치가 곧 압축된 배열의 새로운 길이가 됨
        return write