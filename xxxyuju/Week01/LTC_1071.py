from math import gcd

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        # 두 문자열 길이의 최대공약수
        gcd_len = gcd(len(str1), len(str2))

        # 최대공약수 길이만큼 잘라 후보로 사용
        candidate = str1[:gcd_len]

        # 후보 패턴을 반복했을 때 두 문자열이 모두 만들어지는지 확인
        if candidate * (len(str1) // gcd_len) == str1 and candidate * (len(str2) // gcd_len) == str2:
            return candidate

        # 공통 패턴이 반복되지 않으면 빈 문자열 반환
        return ""