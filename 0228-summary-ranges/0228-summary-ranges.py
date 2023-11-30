class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        
        curr = 0
        ans = []
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1] + 1:
                if curr == i - 1:
                    ans.append(f"{nums[curr]}")
                else:
                    ans.append(f"{nums[curr]}->{nums[i - 1]}")
                curr = i
        if curr == len(nums) - 1:
            ans.append(str(nums[curr]))
        else:
            ans.append(f"{nums[curr]}->{nums[-1]}")
        return ans
                
                    
        