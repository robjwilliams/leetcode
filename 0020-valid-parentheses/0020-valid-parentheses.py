from collections import defaultdict
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) <= 1:
            return False

        stack = []
        dic = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        
        for i in range(len(s)):
            char = s[i]
            peek = stack[-1] if len(stack) else -1
            if char in dic:
                if peek != dic[char]:
                    return False
                stack.pop()
            else: 
                stack.append(char)
 
        return len(stack) == 0
        
        
            