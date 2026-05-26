class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #The Intuition: First, sort the array.
        nums.sort() #sorts in place
        result: list[list[int]] = []

        
        print("Hey")
        
        #Traverse the array, up until the third-to-last element
        for i in range(0, len(nums)-2, 1):
            complement = -1 * nums[i]
            #Do a TwoSum II on the middle elements to try to find the complement
            ptr1 = i + 1 #pointer frmo the next element
            ptr2 = len(nums) - 1 #start from the last element
  
            #try to find the two other nums that sum to the complement
            while(ptr1 < ptr2):
                
                sum = nums[ptr1] + nums[ptr2]
                if sum == complement:
                    
                    result.append([nums[i], nums[ptr1], nums[ptr2]])
                    ptr1 +=1
                    ptr2 -=1 #advance both pointers
                elif sum < complement:
                    ptr1 +=1
                    
                else:
                    ptr2 -=1
                    
                
        result.sort()
        resultsNoDuplicate: List[List[int]] = []
        for i in range(len(result)):
            if(i == len(result)-1 or result[i] != result[i+1]):
                resultsNoDuplicate.append(result[i])
        

        return resultsNoDuplicate