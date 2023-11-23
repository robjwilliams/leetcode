class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        ans = 0
        i = 0
        j = 1
        while i < len(words):
            while j < len(words):
                if words[i] == words[j][::-1]:
                    ans += 1
                j += 1
            i += 1
            j = i + 1

        return ans


                
