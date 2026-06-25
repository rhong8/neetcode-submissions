import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #find the maximum of the array
        max = 0


        for num in piles:
            if num > max:
                max = num #find the maximum

        l, r = 0, max #the fastest time the bananas can be eaten is simply piles.length
        result = max

        #find the first rate that satisfies the hours
        while l <= r and ((l + r) // 2) != 0:
            rate = (l + r) // 2 #the eating banana rate
            #print(f"rate: {rate}")
            time = 0
            for num in piles:
                time += math.ceil(num/rate)
            #print(f"time: {time}")
            if time > h: #takes too long, then we need to increase banana rate
                l = rate + 1
            elif time == h:
                r = rate - 1 #try to make the rate even smaller
                #return rate
            else: #rate is less than the hours
                r = rate - 1
            
            if time <= h:
                result = min(result, rate)

        



        '''
        while l <= r and l != 0:
            print(f"l: {l} r: {r}")
            rate = (l + r) // 2
            print(f"the rate: {rate}")
            time = 0
            for num in piles:
                time += math.ceil(num/rate) #calculate time to eat all the bananas
            if time > h:
                break
            elif time == h:
                return rate
            else: #time is less than, so decrease the rate to find the optimum
                r =  rate - 1
            
            rate = min(rate,result)
        '''
        
        return result        
        

        