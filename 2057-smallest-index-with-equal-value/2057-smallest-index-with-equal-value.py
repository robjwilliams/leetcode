class Solution:
    def smallestEqual(self, nums: List[int]) -> int:
        ans = -1
        for i in range(0, len(nums)):
            curr = i % 10
            if curr == nums[i] and (ans == -1 or i < ans):
                ans = i
        return ans