from typing import List

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counter = Counter(arr)
        if len(counter.values()) != len(set(counter.values())):
            return False
        return True