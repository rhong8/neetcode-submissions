class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
    
        stack = [] #(index,height)
        maxArea = 0 


        for i, val in enumerate(heights):
            #print(f"max area: {maxArea}")
            #print(f"stack: {stack}")
            if not stack or val > stack[-1][1]:
                stack.append((i, val))
            elif val < stack[-1][1]:
                while stack and stack[-1][1] > val:
                    prev_index, prev_height = stack.pop()
                
                #compare areas at that specific point
                    maxArea = max((i - prev_index) * prev_height, maxArea)

                stack.append((prev_index, val)) #valid height up to that point
            else: #val is equal 
                continue

        
        #final sweep
        for pair in stack:
            prev_index = pair[0]
            prev_height = pair[1]

            maxArea = max(prev_height * (len(heights) - prev_index), maxArea)
        
        return maxArea