from collections import Counter
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        counter = Counter(nums)
        ans = 0
        print(counter)
        for n in counter.values():
            ans += n * (n-1) // 2
        
        return ans
        