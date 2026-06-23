class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        dict_cnt = {}

        # 딕셔너리 사용해 고유값과 개수를 key-value로 매핑
        for num in arr:
            if num not in dict_cnt:
                dict_cnt[num] = 0
            dict_cnt[num] += 1


        # set은 중복된 값을 제거하므로 len과 set(len)을 비교해
        # 길이가 같다면 중복된 값이 없는 것이므로 true, 아니면 false
        return len(dict_cnt.values()) == len(set(dict_cnt.values()))
    
s = Solution()
print(s.uniqueOccurrences([1,2,2,1,1,3]))
