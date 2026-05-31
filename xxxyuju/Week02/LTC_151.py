class Solution:
    def reverseWords(self, s: str) -> str:
        # 문자열을 단어 단위로 나누고, 단어 순서를 뒤집어 공백 하나로 연결
        words = s.split()
        return ' '.join(reversed(words))