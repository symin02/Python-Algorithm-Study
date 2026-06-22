class Solution:
    def removeStars(self, s: str) -> str:
        ans = []
        cnt = 0

        for i in range(len(s) - 1, -1, -1):
            if cnt == 0 and s[i] != '*':
                ans.append(s[i])
                continue

            if s[i]  == '*':
                cnt += 1
            else:
                cnt -=1
        ans.reverse()
        return ''.join(ans)