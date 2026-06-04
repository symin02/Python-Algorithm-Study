class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = 'aeiou'
        max_count = 0
        c_count = 0
        left = 0 # 윈도우의 시작 인덱스

        for right in range(len(s)):
            if s[right] in vowels:
                c_count += 1
            if right - left + 1 > k:
                if s[left] in vowels:
                    c_count -= 1
                    
                left += 1

            max_count = max(max_count, c_count)
            
        return max_count
        