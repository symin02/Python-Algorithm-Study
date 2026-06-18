class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        from collections import Counter
        #두 문자열이 가까우려면 1. 길이가 같아야 하고 2. 문자의 종류가 같아야 하고 3. 문자열 종류의 빈도수가 같아야 한다.
        if len(word1)!=len(word2):
            return False
        
        if set(word1)!=set(word2):
            return False

        c1 = Counter(word1)
        c2 = Counter(word2)

        return sorted(c1.values())==sorted(c2.values())
        