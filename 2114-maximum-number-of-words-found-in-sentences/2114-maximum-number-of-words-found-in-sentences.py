class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        curr = 0
        for sentence in sentences:
            sentence_length = len(sentence.split())
            if sentence_length > curr:
                curr = sentence_length 
        return curr