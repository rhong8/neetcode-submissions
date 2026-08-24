import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        h = []
        #create a max heap by pushing the negative value of each stones
        for s in stones:
            heapq.heappush(h, s * - 1)
        
        while len(h) > 1:
            a = -1 * heapq.heappop(h)
            b = -1 * heapq.heappop(h)
        
            new_stone = a - b
            if new_stone != 0:
                heapq.heappush(h, -1 * new_stone)
        
        if not h:
            return 0
        else:
            return h[0] * - 1