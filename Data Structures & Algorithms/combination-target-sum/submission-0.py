class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(path, start):
            if sum(path) == target:
                result.append(path[:])
                return

            # what choices do i have?
            for i in range(start, len(nums)):
                if sum(path) + nums[i] > target:
                    print("Skipping target..")
                    continue
                path.append(nums[i])
                backtrack(path , i) #go to the i index since numbers are allowed to repeat
                path.pop()

        backtrack([], 0)
        return result