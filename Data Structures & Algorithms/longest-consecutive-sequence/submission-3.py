class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums_set = set()
        for num in nums:
            nums_set.add(num)
        res = 1
        
        for n in nums_set:
            if n - 1 not in nums_set:
                temp_len = 0
                x = n
                while x in nums_set:
                    temp_len += 1
                    x += 1

                res = max(res, temp_len)
        
        return res