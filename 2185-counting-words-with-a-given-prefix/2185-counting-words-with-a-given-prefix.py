class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        prefix_count = 0
        for word in words:
            pref_len = len(pref)
            if pref_len <= len(word) and pref == word[:pref_len]:
                prefix_count += 1
        return prefix_count
            