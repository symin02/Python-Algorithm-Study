from collections import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        # 문자 별 갯수를 dict로 저장
        cnt1 = Counter(word1)
        cnt2 = Counter(word2)

        # 문자 종류 비교
        if cnt1.keys() != cnt2.keys():
            return False

        # 문자의 갯수 비교
        if sorted(cnt1.values()) != sorted(cnt2.values()):
            return False

        return True