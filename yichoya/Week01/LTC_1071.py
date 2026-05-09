class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        min_len = min(len(str1), len(str2))

        for k in range(min_len, 0, -1):
            if len(str1) % k != 0 or len(str2) % k != 0:
                continue

            x = str1[:k]
            if x * (len(str1) // k) == str1 and x * (len(str2) // k) == str2:
                return x

        return ""

# sol = Solution()
# sol.gcdOfStrings("BACBACBAC", "BA")

# s = t + t + t + t ...
# 가장 긴 t


