class Solution:
    def reverseWords(self, s: str) -> str:
        sentence = s.split()
        ans = ""
        for word in sentence:
            i = 0
            j = len(word) - 1
            reverse_word = list(word)
            while i < j:
                reverse_word[i], reverse_word[j] = reverse_word[j], reverse_word[i]
                i += 1
                j -= 1
            reverse_word.append(" ")
            ans += "".join(reverse_word)

        return ans.strip()
        
                
        