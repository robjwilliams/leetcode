class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        key_index = {
            'type': 0,
            'color': 1,
            'name': 2
        }
        matches = 0
        for item in items:
            if item[key_index[ruleKey]] == ruleValue:
                matches += 1
        return matches
        