class Solution:
    def makeGood(self, s: str) -> str:
        
        stack = []
        
        for i in range(len(s)):
            char = s[i]
            peek = stack[-1] if len(stack) else ""
            not_great = char.isupper() and peek.islower() or char.islower() and peek.isupper()
            equal_char = char.lower() == peek.lower()

            if not_great and equal_char:
                if stack: stack.pop()
            else:
                stack.append(char)
        
        return "".join(stack)
        