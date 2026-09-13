import heapq
from collections import deque
#heap and queue solution
#it's still o(n) because the possible letters are fixed,
#at most, accessing a letter in a heap is log26, which is o(1) per operation.

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        #array with 26 slots
        counts = [0] * 26

        h = []
        q = deque() #(-1 * count, t it can be added back to heap)

        for t in tasks:
            counts[ord(t.lower()) - ord('a')] += 1
        
        #add all counts to the heap
        for c in counts:
            if c != 0:
                heapq.heappush(h, -1 * c)
        
        #print(h)
        time = 0
        #while heap is nonempty
        while h or q:
            time += 1
            #print(f"time: {time}")
            #print(f"heap: {h}")
            
            #if heap is nonempty, pop it
            if h:
                amt = heapq.heappop(h)
                #print(f"amt: {amt}")
            else:
                amt = 2 #IDLE
                #print("idle this time")
            
            #negative value so we add 1
            #only add it to the queue if we're going to reinsert
            if amt < -1:
                q.append((amt + 1, time + n))
            
            #print(q)
            #add it back to the heap
            if q and time >= q[0][1]:
                heapq.heappush(h, q.popleft()[0])
            

        return time
