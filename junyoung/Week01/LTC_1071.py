class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        # 유클리드 호제법을 통한 최대 공약수  
        def gcd(x, y):
            while y:
                x, y = y, x % y
            return x

        # str1, str2이 똑같은 반복 문자열로 이루어졌는지 확인 
        if str1 + str2 != str2 + str1:
            return ""
        
        # 두 문자열의 최대공약수만큼의 문자열 return
        gcd_len = gcd(len(str1), len(str2))
        return str1[:gcd_len]


s = Solution()
print(s.gcdOfStrings("ABABAB", "ABAB"))