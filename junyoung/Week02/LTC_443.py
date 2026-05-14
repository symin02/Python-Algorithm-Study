from typing import *

class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars) == 1: # 배열 개수가 1이라면 바로 return
            return len(chars)
        
        cnt, i = 1, 1
        alpha = chars[0]    # 알파벳이 같은지 확인하는 용도
        while i < len(chars):
            if alpha == chars[i]:   # 같은 알파벳이 연속되어 나올 경우  
                chars.pop(i)    # i번째 값이 삭제되고 그 다음 원소들이 앞으로 당겨짐
                cnt += 1

            else:   # 다른 알파벳이 나올 경우   
                if cnt > 1: # 알파벳 개수가 1개라면 숫자가 나오지 않으므로 1보다 클 경우만 적용
                    for c in str(cnt):  # cnt를 문자열로 변환 후 한 자리씩 chars에 추가
                        chars.insert(i, c)
                        i += 1  # insert로 인해 현재 i에 새 원소가 들어가고 뒤의 원소들이 뒤로 밀리기 때문에
                                # i를 증가시켜서 자리 맞춤
                alpha = chars[i]
                i+=1
                cnt = 1
                 

        # 구현한 loop에서 마지막 원소의 개수 추가가 포함되지 안흠
        if cnt > 1:
            for c in str(cnt):  # cnt를 문자열로 변환 후 한 자리씩 chars에 추가
                    chars.insert(i, c)
                    i += 1

        print(chars)
        return len(chars)
    
s = Solution()
print(s.compress(["a","a","a","a","a","a","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","c","c","c","c","c","c","c","c","c","c","c","c","c","c"]))
