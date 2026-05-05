class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        # 문자열을 + 연산자로 연결할 때마다 파이썬은 새롭게 임시 객체를 생성해 새 문자열을 만듦
        # -> 연결할 문자열이 많아지면 임시 객체 생성이 많아 메모리가 비효율적
        # string = ""
        # max_length = max(len(word1), len(word2))

        # for i in range(0, max_length):
        #     if i < len(word1):
        #         string += word1[i]
        #     if i < len(word2):
        #         string += word2[i]

        # return ''.join(string)

        # +가 아닌 append를 이용한 풀이
        str_list = []
        pointer1, pointer2 = 0, 0
        while(pointer1 < len(word1) and pointer2 < len(word2)):
            str_list.append(word1[pointer1])
            str_list.append(word2[pointer2])
            pointer1 += 1
            pointer2 += 1
        str_list.append(word1[pointer1:])
        str_list.append(word2[pointer2:])
        
        return ''.join(str_list)

    
s = Solution()
print(s.mergeAlternately("abcd", "pqr"))
