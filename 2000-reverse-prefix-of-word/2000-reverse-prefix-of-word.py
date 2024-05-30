class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        ans = list(word)
        for i in range(0, len(word)):
            if word[i] == ch:
                left = 0
                right = i
                while left < right:
                    ans[left], ans[right] = ans[right], ans[left]
                    left += 1 
                    right -= 1
                return "".join(ans)
            
        return word        