class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        curr = 0
        ans = -1
        for i in range(0, len(nums)):
            curr = abs(i - start)
            if nums[i] == target and (ans == -1 or ans > curr):
                ans = curr
        return ans
                