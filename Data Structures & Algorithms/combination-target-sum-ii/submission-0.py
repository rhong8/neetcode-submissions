class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        candidates.sort()

        def backtrack(path, start):
            
            if sum(path) == target:
                result.append(path[:])
                return
            
            for i in range(start, len(candidates)):
                num = candidates[i]
                if i > start and candidates[i] == candidates[i-1]: #sorted meaning the dupes are right next to eachother
                    continue
                if sum(path) + candidates[i] > target:
                    break #no point in continuing
                

                path.append(candidates[i])
                
                backtrack(path, i + 1) #you can only use each number once
                path.pop()
                
        
        backtrack([], 0)
        return result