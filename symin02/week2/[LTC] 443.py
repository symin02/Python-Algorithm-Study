class Solution:
    def compress(self, chars: list[str]) -> int:
        read = 0  # 읽는 포인터
        write = 0 # 쓰는 포인터
        
        while read < len(chars):
            char = chars[read]
            count = 0
            
            # 같은 문자가 몇 개인지 세기
            while read < len(chars) and chars[read] == char:
                read += 1
                count += 1
            
            # 1. 문자 기록
            chars[write] = char
            write += 1
            
            # 2. 개수가 2개 이상이면 숫자 기록
            if count > 1:
                for s in str(count):
                    chars[write] = s
                    write += 1
                    
        return write
    
if __name__ == "__main__":
    sol = Solution()
    
