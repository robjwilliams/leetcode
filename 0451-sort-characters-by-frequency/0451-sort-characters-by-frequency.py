from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        counter = Counter(s)
        counter = sorted(counter.items(), key=lambda x: x[1], reverse=True)
        ans = [count[0] * count[1] for count in counter]
        
        return "".join(ans)
        