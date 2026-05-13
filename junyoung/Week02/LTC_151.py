class Solution:
    def reverseWords(self, s: str) -> str:
        # 모든 종류의 공백 기준으로 분리
        reverse_str = s.split()

        # 배열 내의 값 순서 바꾸기
        reverse_str.reverse()
        return ' '.join(reverse_str)


s = Solution()
print(s.reverseWords("a good    example"))