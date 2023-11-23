class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans = []
        i = 0
        while i < len(nums):
            ans.append(nums[i]**2)
            i += 1
        ans.sort()
        return ans            
        