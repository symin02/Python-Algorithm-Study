class Solution:
    def decodeString(self, s: str) -> str:
        idx = 0

        def decode():
            nonlocal idx

            res = ""
            num = 0

            while idx < len(s):
                ch = s[idx]

                # 숫자인 경우
                if ch in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                    num = num * 10 + int(ch)

                # [인 경우
                elif ch == '[':
                    idx += 1
                    decoded = decode()
                    res += decoded * num
                    num = 0

                # ]인 경우
                elif ch == ']':
                    return res

                # 문자인 경우
                else:
                    res += ch

                idx += 1
            return res

        return decode()