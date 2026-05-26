class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #always exactly one valid solution, right?


        #compare if solutions are getting warmer
        sum = -1001 #placeholder
        ptr1 = 0
        ptr2 = len(numbers)-1

        while(sum != target):
            #if advancing the left pointer is warmer, advance that
            if numbers[ptr1] + numbers[ptr2] == target:
                return [ptr1 + 1, ptr2 + 1]
            elif abs((numbers[ptr1 + 1] + numbers[ptr2]) - target) < abs((numbers[ptr1] + numbers[ptr2 - 1]) - target): #moving left ptr is warmer
                ptr1 +=1
            else:
                ptr2-=1
            
            #print(f"{ptr1} {ptr2}")



        return [ptr1 + 1, ptr2 + 1]


        




