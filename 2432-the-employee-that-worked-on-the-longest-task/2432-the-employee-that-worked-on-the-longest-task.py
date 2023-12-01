class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        best_employee = logs[0][0]
        longest_duration = logs[0][1]
        for i in range(1, len(logs)):
            current_duration = logs[i][1] - logs[i - 1][1]
            current_employee = logs[i][0]

            if (current_duration == longest_duration and current_employee < best_employee) or current_duration > longest_duration:
                best_employee = current_employee
                longest_duration = current_duration
                
        return best_employee
            
                
                
            
            