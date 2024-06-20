from collections import Counter, defaultdict
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        ans = -1
        counter = Counter(arr)
        for key in counter.keys():
            if key == counter[key]:
                ans = max(ans, key)
        return ans
        