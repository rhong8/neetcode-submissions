class Solution:
    def findMin(self, nums: List[int]) -> int:
        #Optimal Solution
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r)// 2
            if nums[mid - 1] > nums[mid]: #found the pivot
                return nums[mid]
            elif nums[mid] < nums[r]: #it's in the left half
                r = mid - 1
            else: #it's in the right half
                l = mid + 1



        return nums[0]