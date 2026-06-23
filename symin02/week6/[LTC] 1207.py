from typing import List

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count_dict = {}  

        for num in arr:
            if num in count_dict:
                count_dict[num] += 1  # 이미 딕셔너리에 있으면 1 증가
            else:
                count_dict[num] = 1   # 처음 보는 숫자면 개수를 1로 등록
                
        # 딕셔너리에서 숫자들의 등장 횟수만 따로 
        occurrences = count_dict.values()
        
        # 뽑아온 횟수들을 set으로 바꿔서 중복 제거
        if len(set(occurrences)) == len(occurrences):
            return True
        else:
            return False