class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1+str2 != str2+str1:
            return ""

        length = gcd(len(str1),len(str2))
        return str1[:length]

'''
1. 두 문자열이 같은 반복 패턴인지 확인
2. 문자열 길이의 최대공약수(gcd)를 구함
3. 그 길이만큼 앞에서 잘라 반환
'''