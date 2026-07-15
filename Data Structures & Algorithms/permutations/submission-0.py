class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        def backtrack(path):
            if len(path) == len(nums): #base case
                result.append(path[:])
                return
            
            for num in nums:
                if num in path:
                    continue
                path.append(num)
                backtrack(path)
                path.pop() #backtracking step, pop the last element

        
        backtrack([])
        return result