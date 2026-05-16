class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_container = set()
        for num in nums:
            if num in nums_container:
                print(f"{num} is in the string, right?")
                return True
            nums_container.add(num)
            
        
        return False
