class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        count = 0
        for column in range(len(strs[0])):
            for row in range(1, len(strs)):
                if strs[row][column] < strs[row - 1][column]:
                    count += 1
                    break
        return count