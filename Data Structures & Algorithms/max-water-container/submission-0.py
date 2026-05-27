class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ptr1 = 0
        ptr2 = len(heights) - 1
        maxArea = 0

        while(ptr1 < ptr2):
            area = (ptr2 - ptr1) * min(heights[ptr1],heights[ptr2])
            #print(f"area: {area}")
            if area > maxArea:
                maxArea = area
            if heights[ptr1] < heights[ptr2]: #index ptr1 is the smaller height
                ptr1 +=1
                #print(f"ptr1: {ptr1}")
            else: #if the second pillar is taller, or if they are of equal height
                ptr2 -=1
                #print(f"ptr2: {ptr2}")



        return maxArea