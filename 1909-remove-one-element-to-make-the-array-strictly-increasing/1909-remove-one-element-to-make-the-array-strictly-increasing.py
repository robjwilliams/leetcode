class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        removal_count = 0
        for i in range(1, len(nums)):
            if nums[i-1] >= nums[i]:
                removal_count += 1
                if removal_count > 1:
                    return False
                if i > 1 and nums[i-2] >= nums[i]:
                    if i < len(nums) - 1 and nums[i-1] >= nums[i+1]:
                        return False
        return True