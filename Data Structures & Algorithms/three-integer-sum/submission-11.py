class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #The Intuition: First, sort the array.
        nums.sort() #sorts in place
        result: list[list[int]] = []

        
        print("Hey")
        
        #Traverse the array, up until the third-to-last element
        for i in range(0, len(nums)-2, 1):
            if(i != 0 and nums[i] == nums[i-1]):
                continue
            
            complement = -1 * nums[i]
            #Do a TwoSum II on the middle elements to try to find the complement
            ptr1 = i + 1 #pointer frmo the next element
            ptr2 = len(nums) - 1 #start from the last element
  
            #try to find the two other nums that sum to the complement
            while(ptr1 < ptr2):
                
                sum = nums[ptr1] + nums[ptr2]
                if sum == complement:
                    
                    result.append([nums[i], nums[ptr1], nums[ptr2]])
                    while(ptr1 < ptr2) and (nums[ptr1+1] == nums[ptr1] ):
                        ptr1 +=1
                        print(ptr1)
                    while((ptr1 < ptr2) and nums[ptr2-1] == nums[ptr2]):
                        ptr2-=1
                    ptr1 +=1
                    ptr2 -=1 #advance both pointers



                elif sum < complement:
                    ptr1 +=1
                    
                else:
                    ptr2 -=1
                    
                
        result


        return result