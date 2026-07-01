from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        radiant = deque()
        dire = deque()

        for idx, val in enumerate(senate):
            if val == 'R':
                radiant.append(idx)
            else:
                dire.append(idx)

        while radiant and dire:
            r = radiant.popleft()
            d = dire.popleft()

            if r < d:
                radiant.append(r + n)
            else:
                dire.append(d + n)

        if radiant:
            return "Radiant"
        else:
            return "Dire"