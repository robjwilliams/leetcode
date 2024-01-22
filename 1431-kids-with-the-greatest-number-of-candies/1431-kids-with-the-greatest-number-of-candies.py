class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = []
        for kid in candies:
            is_greatest = [kid + extraCandies >= candy for candy in candies]
            result.append(all(is_greatest))
        return result
            
            