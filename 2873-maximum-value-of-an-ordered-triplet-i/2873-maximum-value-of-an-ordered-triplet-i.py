class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        ans = curr = 0
        for i in range(0, len(nums)):
            j = i + 1
            while j < len(nums):
                if j != i:
                    k = j + 1
                    while k < len(nums):
                        if k != j and k != i:
                            curr = (nums[i] - nums[j]) * nums[k]
                            if curr > ans:
                                ans = curr
                        k += 1                    
                j += 1
        return ans