class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        written_lines = 1
        current_line = 0
        for letter in s:
            letter_width = widths[ord(letter) - ord('a')]
            if current_line + letter_width > 100:
                current_line = 0
                written_lines += 1
            current_line += letter_width
            
        return [written_lines, current_line]