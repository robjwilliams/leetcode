class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        i = 0
        j = len(s) - 1
        ans = list(s)
        
        while i < j:
            if ans[i].isalpha() and ans[j].isalpha():
                ans[i], ans[j] = ans[j], ans[i]
                i += 1
                j -= 1
            elif not ans[i].isalpha():
                i += 1
            else:
                j -= 1
        return "".join(ans)