class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ""

        for i in range(0, len(word1)):
            result += word1[i]
            if i < len(word2):
                result += word2[i]
        if len(word2) > len(word1):
            remaining_letters = len(word2)-len(word1)
            result += word2[-remaining_letters:]
            
        return result