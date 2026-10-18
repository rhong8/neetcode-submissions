class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        #either include it or exclude it

        #base case: we have reached the final index

        #constraints
        res = []
        def backtrack(index, path):
            if index == len(nums):
                print(f"appending {path}")
                res.append(path[:])
                return
            


            #Decision 1: include in the array
            path.append(nums[index])
            backtrack(index + 1, path)

            path.pop()
            #decision 2: ddo not include it in the array

            backtrack(index + 1, path)

        
        backtrack(0, [])

        return res
