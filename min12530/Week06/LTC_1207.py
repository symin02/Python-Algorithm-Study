class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counts = {}
        for i in arr:
            if i in counts:
                counts[i] += 1
            else:
                counts[i] = 1
        
        nums = counts.values()
        return len(nums) == len(set(nums))