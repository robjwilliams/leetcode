class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        break_point = -1
        for i in range(1, n):
            if nums[i - 1] > nums[i]:
                break_point = i
                break
        if break_point == -1:
            return True
        
        for i in range(break_point, n - 1):
            print(nums[i], nums[i+1])
            if nums[i] > nums [i+1]:
                return False

        if nums[n - 1] > nums[0]:
            return False
        
        return True
                
            
            