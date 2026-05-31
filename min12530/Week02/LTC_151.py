class Solution:
    def reverseWords(self, s: str) -> str:
        word = s.split()
        # print(word)
        r_word = word[::-1]
        # print(r_word)
        result = ' '.join(r_word)
        # print(result)
        
        return result
        #return ' '.join(reversed(s.split()))