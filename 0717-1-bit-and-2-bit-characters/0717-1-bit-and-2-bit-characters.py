class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        i = 0
        curr = ""
        while i <= len(bits) - 1:
            if i == len(bits) - 1:
                curr = f"{bits[i]}"
            else:
                curr = f"{bits[i]}{bits[i+1]}"
            if curr in ["10", "11"]:
                i += 2
            else:
                curr = f"{bits[i]}"
                i += 1
        return curr == "0"
            