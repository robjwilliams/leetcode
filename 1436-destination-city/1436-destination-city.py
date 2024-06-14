from collections import defaultdict
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        seen = defaultdict(str)
        
        for path in paths:
            seen[path[0]] = path[1]
        
        ans = ""
        for destination in seen.values():
            if destination not in seen:
                ans = destination

        return ans
        