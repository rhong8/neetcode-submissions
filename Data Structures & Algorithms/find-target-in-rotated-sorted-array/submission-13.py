class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #Canonical Solution
        l, r = 0, len(nums) - 1
        
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            
            if nums[mid] < nums[r]: #we're in the right portion, what does that mean
                #split left if the target is greater than the right most value, or less than the current value
                if target > nums[r] or target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else: #we're in the left portion
                #split right if the target is less than the leftmost value, or greater than current
                if target < nums[l] or target > nums[mid]:
                    l = mid + 1
                else:
                    r = mid - 1

        return -1