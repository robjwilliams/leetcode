class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        curr = prev = following = -1

        for i in range(0, len(flowerbed)):
            is_empty = flowerbed[i] == 0
            is_first = i == 0
            is_last = i == len(flowerbed) - 1
            
            curr = flowerbed[i]
            if not is_first:
                prev = flowerbed[i - 1]
            if not is_last:
                following = flowerbed[i + 1]

            if is_first and curr == 0 and following in [0, -1]:
                count += 1
                flowerbed[i] = 1
            elif is_last and curr == 0 and prev == 0:
                count += 1
                flowerbed[i] = 1
            elif prev == 0 and curr == 0 and following == 0:
                count += 1
                flowerbed[i] = 1
      
        return count >= n
            
                