class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        cnt = 0

        # 초기 문자열 s에서 모음이면 1, 아니면 0인 리스트 생성
        arr = [1 if char in vowels else 0 for char in s]

        # 크기가 k인 첫 문자열 확인
        cur = sum(arr[:k])
        ans = cur

        # 슬라이딩
        for i in range(k, len(s)):
            cur += arr[i]
            cur -= arr[i - k]
            ans = max(ans, cur)

        return ans
