class Solution:
    def countSeniors(self, details: List[str]) -> int:
        senior_passangers = [passanger for passanger in details if int(passanger[11:13]) > 60]
        return len(senior_passangers)