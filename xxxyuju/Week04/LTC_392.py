class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_pos = 0

        # 빈 문자열은 어떤 문자열의 부분 수열이든 될 수 있음
        if s == "":
            return True

        # t 순회
        for t_pos in range(len(t)):

            # 현재 s의 문자와 t의 문자가 같으면 s_pos 이동
            if s[s_pos] == t[t_pos]:
                # print(s_pos, t_pos)
                s_pos += 1

            # s의 모든 문자를 찾아냈다면 True
            if s_pos == len(s):
                return True

        return False
        