class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # obvious solution: multiply the entire array, then divide the product by the index
        product_without_zero: int = 1
        zero_count: int = 0
        result: list[int] = [0] * len(nums)

        for num in nums:
            #we already know the entire product will be zero
            if zero_count > 1:
                
                break
            if num == 0:
                zero_count +=1
                print(zero_count)
                continue
            product_without_zero *= num
            

        print(f"product_without_zero: {product_without_zero}")
        if zero_count == 1:
            for i in range(len(nums)):
                if nums[i] == 0:
                    result[i] = product_without_zero
                else:
                    result[i] = 0
        elif zero_count > 1:
            for i in range(len(nums)):
                result[i] = 0
        else: #no zeros  
            for i in range(len(nums)):
                result[i] = int(product_without_zero / nums[i])

        return result