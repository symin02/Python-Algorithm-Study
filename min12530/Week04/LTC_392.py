class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        #s가 비어있다면 부분수열
        if not s: 
            return True

        i = 0
        for char in t:
            if s[i]==char:
                i+=1

                if i==len(s):
                    return True
        
        return False
