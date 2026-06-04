class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max_sum = 0
        sum = 0

        for i in range(len(gain)):
            sum += gain[i]
            max_sum = max(max_sum, sum)

        return max_sum