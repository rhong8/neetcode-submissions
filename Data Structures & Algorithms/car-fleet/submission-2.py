class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #NeetCode's Canonical Solution
        pair = [[p,s] for p,s in zip(position,speed)]

        stack = []
        for p,s in sorted(pair)[::-1]: #iterate in reverse order, starting from greatest position
            stack.append((target - p) / s) #append the time.

            if len(stack) >= 2 and stack[-1] <= stack[-2]: #the topmost element is faster or equal to the one before it.
                stack.pop()

        
        return len(stack)