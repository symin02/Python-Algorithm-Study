class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxcandy = max(candies)

        result = []

        for i in candies:
            if i+extraCandies >= maxcandy:
                result.append(True)
            else:
                result.append(False)
        
        return result