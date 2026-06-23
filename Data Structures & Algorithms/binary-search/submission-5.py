class Solution:
    def search(self, nums: List[int], target: int) -> int:
        idx = int(len(nums) / 2)
        jump = len(nums) / 2
        i = 0
        while idx >= 0 and idx < len(nums) and i < 6:
            if nums[idx] == target:
                return idx
            elif nums[idx] < target:
                idx += int((len(nums) - idx) / 2 + 0.5)
                print(f"going forward to {idx}")
            else:
                idx -= int(idx / 2 + 0.5)
                print(f"going backwards to {idx}")
            i += 1


        
        return -1