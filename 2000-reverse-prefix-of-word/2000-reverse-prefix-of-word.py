class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        i = j = 0
        ans = list(word)
        while i < len(word) and j < len(word):
            if word[j] == ch:
                while i < j:
                    ans[i], ans[j] = ans[j], ans[i]
                    j -= 1
                    i += 1
                return "".join(ans)           
            else:
                j += 1
        
        return "".join(ans)
        