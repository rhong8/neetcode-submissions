class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        

        def isAttacked(r, c):
            #print("Matrix: ", matrix)
            #check if there's a queen on the row
            if 'Q' in matrix[r]:
                return True
            
            #check if there's a queen on the same column
            for row in range(n):
                #print(f"Checking spot {row}, {c}")
                if matrix[row][c] == 'Q':
                    #print(f"Queen found at {row}, {c}" )
                    return True
     
            #Check if there's a queen on the diagonal
            x, y = r, c

            #in bounds
            while x >= 0 and y >= 0 and x < n and y < n:  
                if matrix[x][y] == 'Q':
                    return True
                x += 1
                y += 1
            
            x, y = r, c
            #left-upper diagonal
            while x >= 0 and y >= 0 and x < n and y < n:  
                if matrix[x][y] == 'Q':
                    return True
                x -= 1
                y -= 1
        
            x, y = r, c
            while x >= 0 and y >= 0 and x < n and y < n:  
                if matrix[x][y] == 'Q':
                    return True
                x -= 1
                y += 1
            
            x, y = r, c
            while x >= 0 and y >= 0 and x < n and y < n:  
                if matrix[x][y] == 'Q':
                    return True
                x += 1
                y -= 1
            
           
            return False

        result = []
        positions = [] #array of tuples


        #There only may be one queen per column
        def backtrack(row):
            if row == n: #reached the end of line
                temp = []
                for j in range(n):
                    temp.append("".join(matrix[j]))
                    
                result.append(temp)
                return
            
            for col in range(n):
                
                if not isAttacked(row, col):
                    print(f"This spot isn't attacked. Placing Q on {row} {col}")
                    matrix[row][col] = 'Q'
                    backtrack(row + 1)
                    matrix[row][col] = '.' #cleanup
                
        matrix = [['.' for _ in range(n)] for _ in range(n)]
        
        backtrack(0)
        return result

            
                                    