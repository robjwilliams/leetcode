from collections import defaultdict
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dict1 = defaultdict(str)
        dict2 = defaultdict(str)
        
        for i in range(len(s)):
            if s[i] not in dict1:
                dict1[s[i]] = t[i]
            if t[i] not in dict2:
                dict2[t[i]] = s[i]
        print(dict1)
        print(dict2)
        for i in range(len(s)):
            print(dict1[s[i]], t[i], '--', dict2[t[i]], s[i])
            if dict1[s[i]] != t[i] or dict2[t[i]] != s[i]:
                return False
            # print(s[i] in dict2, t[i] in dict1)
        # for i in range(len(s)):
        #     print(t[i], dict2[t[i]])
        
        return True
        
        
        