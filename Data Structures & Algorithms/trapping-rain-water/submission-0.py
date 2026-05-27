class Solution:
    def trap(self, height: List[int]) -> int:
        #trapping rain water right?`
        ptr1 = 0
        ptr2 = len(height) - 1
        temp_height: int
        #temp_area_stack = []
        ans = 0

        while(ptr1 < ptr2):
            if height[ptr1] <= height[ptr2]:
                temp_height = height[ptr1]
                ptr1 += 1
                while(ptr1 < ptr2 and height[ptr1] < temp_height):
                    #temp_area_stack.append(temp_height - height[ptr1])
                    ans += (temp_height - height[ptr1])
                    ptr1 +=1
            else:
                temp_height = height[ptr2]
                ptr2 -= 1
                while(ptr1 < ptr2 and height[ptr2] < temp_height):
                    #temp_area_stack.append(temp_height - height[ptr2])
                    ans += (temp_height - height[ptr2])
                    ptr2 -=1
        


        return ans
    

                