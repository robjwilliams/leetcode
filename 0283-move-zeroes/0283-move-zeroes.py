class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = 1
        
        while i < len(nums) - 1:
            # Move pointer i to the next non-zero element
            while i < len(nums) - 1 and nums[i] != 0:
                i += 1

            # Move pointer j to the next non-zero element after i
            j = max(j, i + 1)
            while j < len(nums) - 1 and nums[j] == 0:
                j += 1

            # If nums[i] is zero and nums[j] is non-zero, swap them
            if i < len(nums) and j < len(nums):
                if nums[i] == 0 and nums[j] != 0:
                    nums[i], nums[j] = nums[j], nums[i]

            i += 1
            j += 1
            
            
            
            
        