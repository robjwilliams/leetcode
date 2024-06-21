from collections import Counter, defaultdict
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        dict1 = defaultdict(int)
        dict2 = defaultdict(int)
        words = s.split()
        if len(pattern) != len(words): return False
        for i in range(0, len(pattern)):
            curr = pattern[i]
            word = words[i]
            if not curr in dict1:
                dict1[curr] = word

        for i in range(0, len(pattern)):
            curr = pattern[i]
            word = words[i]
            if not word in dict2:
                dict2[word] = curr
            if dict1[curr] != word or dict2[word] != curr:
                return False
            print(dict1[curr], word, '--',dict2[word], curr)
        
        print(dict1, dict2)
            
        
        
        return True
        