class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split() #공백을 기준으로 단어만 추출해서 리스트로 만든다.
                          #문자열을 공백 기준으로 쪼갭니다. 이때 인자 없이 .split()을 쓰면 연속된 공백이나 앞뒤 공백을 알아서 다 제거하고 단어만 리스트에 담아줍니다.
        words.reverse() #리스트의 순서를 뒤집는다.

        return " ".join(words)
    
sol = Solution()
print(sol.reverseWords(" hello world"))
print(sol.reverseWords(" a good example"))