class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        cnt = 0

        # 모음을 탐색 시 O(1)로 빨리 탐색하기 위해 hash 자료구조인 set 사용
        vowels = set('aeiou')

        # 초기 k길이만큼의 모음 개수
        for i in range(k):
            if s[i] in vowels:
                cnt += 1

        max_cnt = cnt
        for e in range(k, len(s)):

            # 윈도우 제거되는 부분이 모음이면 cnt - 1
            if s[e - k] in vowels:
                cnt -= 1
            # 윈도우에 추가되는 부분이 모음이면 cnt + 1
            if s[e] in vowels:
                cnt += 1
            
            max_cnt = max(max_cnt, cnt)

            # k 길이와 최대 cnt가 같다면 즉시 return
            if max_cnt == k:
                return max_cnt
        
        return max_cnt
    
s = Solution()
print(s.maxVowels("leetcode", 3))
