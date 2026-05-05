class Solution:
    def reverseVowels(self, s: str) -> str:
        # lower_vowels = ['a', 'e', 'i', 'o', 'u']
        # upper_vowels = ['A', 'E', 'I', 'O', 'U']

        # # 문자열 -> 배열 변환
        # s = list(s) 
        # vowels_index_arr = []

        # i=0
        # while i < len(s):
        #     if s[i] in lower_vowels or s[i] in upper_vowels:
        #         vowels_index_arr.append(i)
        #     i += 1

        # vowels_count = len(vowels_index_arr)
        # for i in range(0, vowels_count // 2):
        #     tmp = s[vowels_index_arr[i]]
        #     s[vowels_index_arr[i]] = s[vowels_index_arr[vowels_count - i - 1]]
        #     s[vowels_index_arr[vowels_count - i - 1]] = tmp

        # return ''.join(s)


        ## 투 포인터를 이용해 구하기 ##
        # List: 배열로 구현, 순차 인덱스로 접근하기 때문에 삽입/제거/탐색 시간복잡도 O(n) 
        # set: Hash table로 구현, 중복값 허용x, 값에 대한 고유 hash 코드를 기반으로 저장하기 때문에 시간복잡도 O(1) 
        vowels = set("aeiouAEIOU")
        result = list(s)

        start = 0
        end = len(s) - 1

        # 시작 인덱스/끝 인덱스가 서로 모음을 찾을때까지 반복, 찾으면 서로 위치 이동
        while start < end:
            if s[start] not in vowels:
                start += 1
            elif s[end] not in vowels:
                end -= 1
            else:
                result[start], result[end] = result[end], result[start]
                start += 1
                end -= 1
        return ''.join(result)
    
s = Solution()
str = "IceCreAm"
print(s.reverseVowels(str))