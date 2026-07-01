from collections import Counter 

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # counter로 등장 횟수 세기
        counter1 = Counter(word1)
        counter2 = Counter(word2)
        
        # 키 값들만 뽑아서 정렬 후 알파벳 종류가 같은지 비교
        if sorted(counter1.keys()) != sorted(counter2.keys()):
            return False
            
        # 등장 횟수 비교
        if sorted(counter1.values()) != sorted(counter2.values()):
            return False
            
        return True