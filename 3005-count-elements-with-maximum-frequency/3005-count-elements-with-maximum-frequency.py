from collections import defaultdict
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        frequencies = defaultdict(int)
        
        for num in nums:
            frequencies[num] += 1
            
        ans = count = max_freq = 0
        count = defaultdict(int)
        for num in frequencies.keys():
            if frequencies[num] > max_freq:
                max_freq = frequencies[num]
            frequency = frequencies[num]
            count[frequency] += frequency

        ans = count[max_freq]

        return ans
        