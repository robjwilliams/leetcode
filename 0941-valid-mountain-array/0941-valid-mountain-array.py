class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3 or arr[0] >= arr[1]:
            return False
        reached_top = False
        for i in range(0, len(arr) - 1):
            if arr[i] < arr[i+1] :
                if reached_top:
                    return False 
            elif arr[i] > arr[i+1]:
                if not reached_top:
                    reached_top = True
                elif i == len(arr) - 2:
                    return True
            else:
                return False

        return reached_top
            