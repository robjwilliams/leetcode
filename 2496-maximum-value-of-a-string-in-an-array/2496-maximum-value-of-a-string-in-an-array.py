class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        maximum_value = 0
        for value in strs:
            try:
                if int(value) > maximum_value:
                    maximum_value = int(value)
            except ValueError:
                if len(value) > maximum_value:
                    maximum_value = len(value)
        return maximum_value