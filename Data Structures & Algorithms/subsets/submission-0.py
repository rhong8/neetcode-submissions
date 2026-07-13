class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(index, path):
            
            if index == len(nums):
                result.append(path[:]) # a copy of path
                return
            
            #decision 1, include in the subtree
            path.append(nums[index])
            backtrack(index + 1, path)
            
            path.pop() #UNDO THAT

            #decision 2, DON'T include in the subtree, advance the index
            backtrack(index + 1, path)
        
        backtrack(0, [])

        return result