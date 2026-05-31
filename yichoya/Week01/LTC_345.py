class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u']
        tmp = []
        string = list(s)

        for i in range(0, len(s)):
            char = string[i].lower()
            if char in vowels:
                tmp.append(string[i])

        for i in range(0, len(s)):
            char = string[i].lower()
            if char in vowels:
                string[i] = tmp.pop()

        return ''.join(string)
