class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        ans = None
        for i in range(0, len(nums)):
            if ans is None or abs(ans) > abs(nums[i]):
                ans = nums[i]
            elif abs(ans) == abs(nums[i]):
                ans = nums[i] if ans < nums[i] else ans
                
        return ans