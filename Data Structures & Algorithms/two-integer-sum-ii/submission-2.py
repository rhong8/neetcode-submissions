class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        ptr1 = 0
        ptr2 = len(numbers)-1
        sum: int = 0

        while(ptr1 < ptr2):
            sum = numbers[ptr1] + numbers[ptr2]
            if(sum == target):
                return [ptr1+1, ptr2+1]
            elif(sum < target):
                ptr1 +=1
            else:
                ptr2 -=1


        return [ptr1 +1, ptr2 +1]