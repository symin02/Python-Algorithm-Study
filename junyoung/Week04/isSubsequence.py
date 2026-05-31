class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_pointer, t_pointer = 0, 0
        s_len = len(s)
        t_len = len(t)

        if s_len == 0:
            return True

        s_pointer = 0
        for t_pointer in range(t_len):
            if s_pointer == s_len:
                return True
            if s[s_pointer] == t[t_pointer]:
                s_pointer += 1
        if s_len != s_pointer:
            return False
        else:
            return True
        
s = Solution()
print(s.isSubsequence("abc", "ahbgdc"))
