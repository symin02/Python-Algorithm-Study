class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # 두 문자열을 같은 인덱스끼리 묶어 번갈아 이어 붙이기
        res = ''.join(a + b for a, b in zip(word1, word2))

        # 남은 부분 붙이기
        return res + word1[len(word2):] + word2[len(word1):]