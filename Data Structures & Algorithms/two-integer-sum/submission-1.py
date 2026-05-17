class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        #this dictionary
        #keys:  target - each integer.
        #value: index of which it was found 
        differences = {}
        result: list[int] = []
        
        #if the loop finds the "difference", then it returns the result
        for i in range(len(nums)):
            if(nums[i] in differences):
                print("found!!")
                result.append(differences[nums[i]])
                result.append(i)
                break
            else:
                differences[target - nums[i]] = i


        return result
