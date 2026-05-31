class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
    
        pairs = sorted(zip(position, speed), reverse=True) #sorted in reserve order

        #start from the highest position.
        for p, s in pairs:
            #calculate the time to reach the destination
            time = (target - p) / s
            print(time)
            if not stack or time > stack[-1]: #if the time to reach the target is greater, add it to the stack
                stack.append(time)
        


        
        return len(stack)
        

