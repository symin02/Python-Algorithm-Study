from collections import Counter
from typing import List
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:

        counter = Counter(arr)

        # 등장 횟수만 모아서 중복 제거
        counter_set = set([x for x in counter.values()])

        # 숫자 개수와 등장 횟수의 개수가 같으면 true
        return len(counter_set) == len(counter)

        