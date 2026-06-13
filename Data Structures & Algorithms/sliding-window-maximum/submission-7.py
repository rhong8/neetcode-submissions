class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        from collections import deque

        #initiailize 
        d = deque() 
        results = []
        
        '''
        j = 0
        for i in range(k):
            value = nums[i]

            #sort in decreasing order, but put the index
            for j in range(len(d)):
                print(f"entering loop at {j}, {value} " )
                if value < nums[d[j]]:
                    j += 1
            d.insert(j, i)
        '''
        
             


        #dequeue is ready.
        
        #the last beginning of the window is at len(nums) - k, right?
        for i in range(len(nums)):
            #last element of the window
            
            #new_last = i + k - 1
            #print("new last: ", new_last)

            #is greater than the previous elements
            while d and nums[i] > nums[d[-1]]:
                d.pop()
            d.append(i)

            if d[0] < i - k + 1:
                d.popleft() #pop a maximum if its stayed past it

            #keep popping if the maximum has expired already, iterate till the end
            if i >= k - 1:
                results.append(nums[d[0]])

            
            

        #For this array, check the index in the max position to see if its ready to leave.
        return results
        
            
            