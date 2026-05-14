class Solution:
    def isValid(self, s: str) -> bool:
        map = {")":"(","}":"{", "]":"["}
        stack = []
        for c in s:
            if c in ["(", "{", "["]:
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False

                top = stack.pop()
                if map[c] != top:
                    return False
        if len(stack) != 0:
            return False
        return True