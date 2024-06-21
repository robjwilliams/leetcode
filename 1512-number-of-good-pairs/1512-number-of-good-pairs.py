from collections import Counter
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        counter = Counter(nums)
        ans = 0

        for n in counter.values():
            ans += n * (n-1) // 2
        
        return ans
        