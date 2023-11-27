class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        is_acronym = []
        if len(s) == len(words):
            for i, word in enumerate(words):
                is_acronym.append(word[0] == s[i])
        return all(is_acronym) and len(is_acronym)
        