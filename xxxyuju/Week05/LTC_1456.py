class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set('aeiou')   # 모음 저장

        chars = s[:k]
        max_num = 0
        cnt = 0

        for char in chars:
            if char in vowels:
                cnt += 1

        max_num = cnt
        left = 1
        right = k

        while right < len(s):
            if max_num == k:    # 가능한 최댓값이면 종료
                return k

            if s[left-1] in vowels: # 빠지는 문자
                cnt -= 1

            if s[right] in vowels:  # 들어오는 문자
                cnt += 1

            max_num = max(max_num, cnt)
            left += 1
            right += 1

        return max_num
                