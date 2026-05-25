class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        idx_s = 0

        for ch in t:
            if idx_s < len(s) and s[idx_s] == ch:
                idx_s += 1

        if idx_s == len(s):
            return True
        return idx_s == len(s)