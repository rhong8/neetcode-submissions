import numpy as np
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        seen: List[List[Bool]] =  [[False] * COLS for _ in range(ROWS)]
        #right,down,left,up,right 
        turn = {(0, 1): (1, 0), (1, 0): (0, -1), (0, -1): (-1, 0), (-1, 0): (0, 1)}
    
        def valid(x,y):
            return x in range(ROWS) and y in range(COLS) and seen[x][y] == False
        
        array = []
        def spiral(i, j, direction):
            if len(array) == ROWS * COLS:
                return

            if not valid(i, j):
                i, j = i - direction[0], j - direction[1]
                direction = turn[direction]
                i, j = i + direction[0], j + direction[1]
                spiral(i, j, direction)

            else:
                array.append(matrix[i][j])
                seen[i][j] = True
                spiral(i + direction[0], j + direction[1], direction)

        
        spiral(0, 0, (0,1))
        return array

        