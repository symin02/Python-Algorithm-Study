class Solution:
    def reverseWords(self, s: str) -> str:
        words = list(s.split())
        words_reversed = words[::-1]
        return " ".join(words_reversed)
