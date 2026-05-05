class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        max_candy = max(candies)

        result = []
        
        for candy in candies:
            if candy + extraCandies >= max_candy:
                result.append(True)
            else:
                result.append(False)

        return result
    
sol = Solution()
print(sol.kidsWithCandies([2, 3, 5, 1, 3], 3))