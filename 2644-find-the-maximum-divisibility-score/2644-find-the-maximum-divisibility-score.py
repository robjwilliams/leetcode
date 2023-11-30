class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        curr = 0
        ans = [-1, 0]
        for i in range(0, len(divisors)):
            for j in range(0, len(nums)):
                if nums[j] % divisors[i] == 0:
                    curr += 1
            if ans[0] == -1 or curr > ans[1] or (curr == ans[1] and divisors[i] < ans[0]):
                ans = [divisors[i], curr]
            curr = 0
                
                
        return ans[0]