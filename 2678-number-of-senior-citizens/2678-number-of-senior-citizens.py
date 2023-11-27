class Solution:
    def countSeniors(self, details: List[str]) -> int:
        return len([passanger for passanger in details if int(passanger[11:13]) > 60])