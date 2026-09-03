class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Quickselect solution
        k_ind = len(nums) - k  # index of kth largest in sorted-ascending order

        def quickselect(l, r):
            pivot, p = nums[r], l
            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[i], nums[p] = nums[p], nums[i]
                    p += 1  # increment pointer by 1
            nums[p], nums[r] = nums[r], nums[p]

            if p < k_ind:
                return quickselect(p + 1, r)
            elif p > k_ind:
                return quickselect(l, p - 1)
            else:
                return nums[p]

        return quickselect(0, len(nums) - 1)