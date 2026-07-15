class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        def backtrack(path, start):
            result.append(path[:])
            if start == len(nums):
                
                return
            
            #What decisions do i have?

            
            #Include it in the tree
            for i in range(start, len(nums)):
                #Exclude at the same depth
                if i > start and nums[i] == nums[i - 1]:
                    continue
                
                path.append(nums[i])
                backtrack(path, i + 1)
                path.pop()

            

    

        backtrack([], 0)
        return result