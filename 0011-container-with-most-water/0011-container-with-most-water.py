class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = ans = 0
        j = len(height) - 1

        while i < j:
            x = j - i
            
            if height[i] < height[j]:
                y = height[i]
                i += 1
            else:
                y = height[j]
                j -= 1

            volume = x * y
            ans = max(ans, volume)
        return ans
            
        