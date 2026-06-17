from collections import Counter
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:

        counter1 = Counter(word1)
        counter2 = Counter(word2)

        # 사용한 문자의 종류가 다르면 False
        if sorted(counter1.keys()) != sorted(counter2.keys()):
            return False

        # 문자가 나온 횟수의 구성이 다르면 False
        if sorted(counter1.values()) != sorted(counter2.values()):
            return False

        return True