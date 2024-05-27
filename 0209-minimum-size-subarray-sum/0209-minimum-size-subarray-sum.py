class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = curr = ans = 0
        for right in range(0, len(nums)):
            curr += nums[right]
            
            while curr >= target:
                if ans == 0:
                    ans = right - left + 1
                ans = min(ans, right - left + 1)
                curr -= nums[left]
                left += 1
    
        return ans