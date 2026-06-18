class Solution:
    def removeStars(self, s: str) -> str:
        answer = []

        for i in s:
            if i == '*':
                answer.pop()
            else:
                answer.append(i)
        
        return "".join(answer)