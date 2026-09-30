import heapq
class MedianFinder:

    def __init__(self):
        
        self.l_side = [] #maintain a maxHeap
        self.r_side = [] #maintain a minHeap
        self.median = 0

    def addNum(self, num: int) -> None:
        
        #multiply by -1
        if num > self.median:
            heapq.heappush(self.r_side,  num)
        else:
            heapq.heappush(self.l_side, -1 * num)
        
        if len(self.l_side) > len(self.r_side) + 1:
            val = heapq.heappop(self.l_side)
            heapq.heappush(self.r_side, -1 * val)
        elif len(self.r_side) > len(self.l_side) + 1:
            val = heapq.heappop(self.r_side)
            heapq.heappush(self.l_side, -1 * val)
        
    
        if (len(self.l_side) + len(self.r_side)) % 2 == 0:
            #print("even amt")

            self.median = (-1 * self.l_side[0] + self.r_side[0]) / 2.0
        else:
            if len(self.l_side) > len(self.r_side):
                self.median = -1 * self.l_side[0]
            else:
                self.median = self.r_side[0]

        #print(f"l side tree: {self.l_side}")
        #print(f"r side tree: {self.r_side}")
        #print("New median: ", self.median)
        

    def findMedian(self) -> float:
        #print("self")
        return self.median
        
        