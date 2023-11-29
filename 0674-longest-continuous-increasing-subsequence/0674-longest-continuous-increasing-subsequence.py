class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        curr = 1
        ans = 1
        j = 0
        for i in range(0, len(nums) - 1):
            if nums[j + 1] > nums[i]:
                curr += 1
            else:
                curr = 1
            if curr > ans:
                ans = curr
            j += 1
        return ans