class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        ans = -1
        j = len(nums) - 1
        for i in range(0, len(nums)):
            while j >= 0:
                if i < j and nums[j] > nums[i] and (nums[j] - nums[i]) > ans:
                    ans = nums[j] - nums[i]
                j -=1
            j = len(nums) - 1
            
        return ans