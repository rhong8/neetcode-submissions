class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #solution without division
        forwards: list[int] = [1] * len(nums)
        forward_product = 1
        backwards: list[int] = [1] * len(nums)
        backwards_product = 1

        for i in range(len(nums)):
            forwards[i] = forward_product * nums[i]
            forward_product = forward_product * nums[i]
        
        for k in range(len(nums)-1, -1, -1):
            
            backwards[k] = backwards_product * nums[k]
            backwards_product = backwards[k]


        #putting together the solution now. the formula is f[i-1] * b[i+1], given that
        # forward[i-1] represents the product of numbers before the current index, and b[i+1]
        #represents the product of values afterwards. if i-1 or i+1 is out of bounds they are replaced by 1.
        result: list[int] = [1] * len(nums)
        for i in range(len(nums)):
            if i == 0:
                result[i] = backwards[1]
            elif i == len(nums)-1:
                result[i] = forwards[i-1]
            else:
                result[i] = forwards[i-1] * backwards[i+1]

        del forwards
        del backwards

        return result
