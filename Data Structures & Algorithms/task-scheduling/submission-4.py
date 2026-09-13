import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        max_count = 0
        nums_max = 0
        #the number of elements at exactly max
        counts = defaultdict(int)
 
        for t in tasks:
            counts[t] += 1
            if counts[t] == max_count:
                nums_max += 1
            elif counts[t] > max_count:
                max_count = counts[t]
                nums_max = 1    
        
        #initial number of slots is constrained by
        #max_count + (n * (max_count - 1)
        init = max_count + n * (max_count - 1) + nums_max - 1
        

     

        res = max(init, len(tasks))

        return res

                
