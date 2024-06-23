from collections import OrderedDict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        left = ans = curr = 0
        seen = OrderedDict()
        
        for right in range(n):
            curr += 1
            while s[right] in seen:
                del seen[s[left]]
                left += 1
                curr -= 1
            seen[s[right]] = right
            ans = max(ans, curr)
            # print(seen, curr)

        return ans
            
        