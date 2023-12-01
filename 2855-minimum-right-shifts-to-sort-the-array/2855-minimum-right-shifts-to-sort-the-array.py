class Solution:
    def minimumRightShifts(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        break_point = -1

        for i in range(1, n):
            if nums[i - 1] > nums[i]:
                break_point = i
                break

        if break_point == -1:
            return 0

        for i in range(break_point, n - 1):
            if nums[i] > nums[i + 1]:
                return -1
        
        if nums[n - 1] > nums[0]:
            return -1
        
        return len(nums) - break_point
