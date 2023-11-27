class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        truncatedSentence = s.split(' ')[:k]   
        return ' '.join(truncatedSentence)