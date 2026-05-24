class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
    
        longest = 0

        nums_set = set(nums)
        
        for k in range(len(nums)):
            if(nums[k] - 1 not in nums_set): 
                #then it's a starting point
                x = nums[k]
                print(f"x: {x}")
                #part of the sequence
                temp = 0
                while(x in nums_set):   
                    temp += 1
                    x += 1
                    print(temp)
                    if(temp > longest):
                        longest = temp

        
                temp = 0



        print(f"longest at the end: {longest}")
        return longest





 