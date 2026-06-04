from typing import List

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        alt = [0] * (len(gain) + 1)

        for i in range(len(gain)):
            alt[i + 1] = alt[i] + gain[i]
        return max(alt)