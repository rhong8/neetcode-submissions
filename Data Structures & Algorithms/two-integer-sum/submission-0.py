class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        #this dictionary
        #keys:  target - each integer.
        #value: index of which it was found 
        differences = {}
        result: list[int] = []
        
        for i in range(len(nums)):
            if(nums[i] in differences):
                print("found!!")
                result.append(differences[nums[i]])
                result.append(i)
                break
            else:
                differences[target - nums[i]] = i

        print(differences.keys())
        print(differences.values())
        return result
