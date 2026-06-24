class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        top, bot = 0, ROWS - 1
        
        while top <= bot:
            row = (top + bot) // 2
            #case that the value is larger than the greatest value of the array
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]: #value is smaller than smallest value
                bot = row - 1
            else:
                break
        
        print(f"{(top + bot) // 2}, top {top}, bot {bot}")


        if not (top <= bot): #out of bounds
            print("hello")
            return False
        

        row = (top + bot) // 2
        l, r = 0, COLS - 1
        
        while l <= r:
            mid = (l + r) // 2
            if matrix[row][mid] == target:
                return True
            elif target > matrix[row][mid]:
                l = mid + 1
            else: 
                r = mid - 1
        
        print("hey")
        return False