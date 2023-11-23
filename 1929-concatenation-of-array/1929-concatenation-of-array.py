class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = nums.copy()
        i = 0
        while i < len(nums):
            ans.append(nums[i])
            i += 1
        return ans