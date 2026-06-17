class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #treat it as an array of indices, and use cycle detection

        slow = nums[0]
        fast = nums[0]

        # Phase 1: Finding the intersection point in the cycle
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        # Phase 2: Finding the entrance to the cycle (the duplicate)
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow