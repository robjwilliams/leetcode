class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        ans = [0, releaseTimes[0]]
        for i in range(0, len(releaseTimes)):
            if i == 0:
                duration = releaseTimes[i]
            else:
                duration = releaseTimes[i] - releaseTimes[i - 1]
            
            if (duration == ans[1] and keysPressed[i] > keysPressed[ans[0]]) or duration > ans[1]:
                ans = [i, duration]
            
        return keysPressed[ans[0]]