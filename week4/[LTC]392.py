class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_idx = 0
        t_idx = 0

        # 두 포인터 중 어느 하나라도 문자열 끝에 도달하면 반복 종료
        while s_idx < len(s) and t_idx < len(t):
            # 두 글자가 일치하면, s의 다음 글자를 찾으러 s_idx 이동
            if s[s_idx] == t[t_idx]:
                s_idx += 1

        # t의 포인터는 일치하든 안 하든 매 턴마다 무조건 이동
            t_idx += 1
        # s의 모든 글자를 순서대로 다 찾았다면 s_idx가 len(s)와 같아짐
        return s_idx == len(s)
    