class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_stack = []
        t_stack = []
        
        for i in range(len(s)):
            char = s[i]
            if char == '#':
                if len(s_stack): s_stack.pop()
            else:
                s_stack.append(char)
        
        for i in range(len(t)):
            char = t[i]
            if char == '#':
                if len(t_stack): t_stack.pop()
            else:
                t_stack.append(char)
        
        return s_stack == t_stack
            
        