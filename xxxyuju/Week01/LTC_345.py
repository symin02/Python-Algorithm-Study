class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "aeiouAEIOU"

        # 모음이 있는 인덱스만 추출
        idx = [i for i, ch in enumerate(s) if ch in vowels]

        s = list(s)
        i, j = 0, len(idx) - 1

        # 모음 위치의 양 끝부터 바꿔가며 swap
        while i < j:
            s[idx[i]], s[idx[j]] = s[idx[j]], s[idx[i]]
            i += 1
            j -= 1

        return ''.join(s)
        