import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #Canonical Solution

        l, r = 1, max(piles)
        result = r

        while l <= r:
            k = (l + r) // 2
            time = 0
            for p in piles:
                time += math.ceil(p / k) 
            
            if time <= h: #in time
                result = min(result, k) 
                r = k - 1 #search for a lower rate
            else:
                l = k + 1

        return result