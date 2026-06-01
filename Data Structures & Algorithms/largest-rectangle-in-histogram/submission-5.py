class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] #(index, value)
        maxArea = 0

        for i, value in enumerate(heights):
            start = i
            while stack and value <= stack[-1][1]:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))
                start = index #update the start index
            
            print(f"pair: {start},{value}")
            stack.append((start, value))
        print(stack)

        #final clean up
        for i, height in stack:
            maxArea = max(maxArea, (len(heights) - i) * height)

        return maxArea