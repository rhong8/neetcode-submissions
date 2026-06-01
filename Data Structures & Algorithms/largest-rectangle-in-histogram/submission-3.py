class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0
        previousValue = 0
        startingIndex = 0
        for i, value in enumerate(heights):
            #print(f"stack:  {stack}")
            #as long as the values are increasing, push the value and starting index.
            if not stack or value >= stack[-1][0]: 
                #print(f"Adding: {value}, {i}")
                stack.append((value, i))
            else: #value is smaller
                #print(f"smaller element encountered: {value}")
                while stack and value <= stack[-1][0]: #go until you hit the starting index of a preivous
                    previousValue, startingIndex = stack.pop()
                    area = (i - startingIndex) * previousValue
                    #print(area)
                    maxArea = max(maxArea, (i - startingIndex) * previousValue)
                    #print(f"MaxArea: Either {area} or {maxArea}")
                    #keep track of the latest starting index
                #print(f"Adding (Finished Process): {value}, {startingIndex}")
                
                #print(f"clearstack?: {stack}")
                stack.append((value, startingIndex)) #the histogram has a minimum height that reaches that far

            if i == len(heights)-1:
                #print("entering the end game")
                
                while stack:
                    
                    #print(stack)
                    previousValue, startingIndex = stack.pop()
                    area = (len(heights) - startingIndex) * previousValue
                    #print(f"Either {maxArea} or {area}")
                    maxArea = max(maxArea, (len(heights) - startingIndex) * previousValue)
                    
                
                #value is smaller. then pop backwards, subtract current index - starting to find area.

        return maxArea