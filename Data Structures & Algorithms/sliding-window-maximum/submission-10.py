class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        #Neetcode's Canonical Solution
        from collections import deque

        q = deque() #Deque that stores indices
        res = []

        l = r = 0 #Both start at 0

        while r < len(nums):
            #Deque that stores decreasing values
            #Pop all the values that are less than in the window, that came before
            #Because it's not going to be considered.
            #We still append lesser elements that come after, because they may be the future max.
            while q and nums[r] > nums[q[-1]]:
                q.pop()
            q.append(r)

            #Remove the maximum element if it's out of bounds
            if q[0] < l:
                q.popleft()

            #Finally, if the right pointer is sufficiently at a window size,
            #Append the maximum of that window.
            if r + 1 >= k:
                res.append(nums[q[0]])
                #print(f"appending {nums[q[0]]}")
                l += 1
            r += 1
            #print(q)
        
        return res