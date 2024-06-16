class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        
        for i in range(len(s)):
            letter = s[i]
            peek = stack[-1] if stack else -1
            
            if peek == letter:
                stack.pop()
            else:
                stack.append(letter)
        
        return "".join(stack)
        