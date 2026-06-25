class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        mid = (l + r) // 2
        while l <= r:
            
            mid = (l + r) // 2
            if (mid == 0 and nums[-1] > nums[0]) or (nums[mid - 1] > nums[mid]):
                return nums[mid]
            elif nums[mid] < nums[r]: #it's in the left half, split it
                
                r = mid -1
            else:
                l = mid + 1

        return nums[mid]