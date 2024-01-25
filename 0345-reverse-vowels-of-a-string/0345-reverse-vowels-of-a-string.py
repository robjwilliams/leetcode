class Solution:
    def reverseVowels(self, s: str) -> str:
        s_list = list(s)
        vowels = set("aeiouAEIOU")
        i = 0
        j = len(s) - 1
        
        while i < j:
            while i < j and s_list[i].lower() not in vowels:
                i += 1
            while i < j and s_list[j].lower() not in vowels:
                j -= 1

            s_list[i], s_list[j] = s_list[j], s_list[i]

            i += 1
            j -= 1

        return "".join(s_list)
                
            