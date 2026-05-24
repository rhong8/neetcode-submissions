class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        #first check all the rows to make sure they don't have duplicates
        
        for row in range(9): #controlling rows
            row_container = set()
            for col in range(9): #controlling cols
                if(board[row][col] == "."):
                    continue
                if(board[row][col] in row_container):
                    return False
                row_container.add(board[row][col])

        
        #next check all the cols to make sure they don't have duplicates
        for col in range(9):
            col_container = set()
            for row in range(9):
                if(board[row][col] == "."):
                    continue

                if(board[row][col] in col_container):
                    return False
                col_container.add(board[row][col])

        #last check all the sub boxes
        
        #iterate through the sub boxes, incrementing "sub-col wise"
        for outer_row in range(3):
            for outer_col in range(3):
                sub_box_container = set()
                #loop through the INNER rows
                for inner_row in range(3):
                    for inner_col in range(3):
                        element = board[outer_row * 3 + inner_row][outer_col * 3 + inner_col]
                        if(element == "."):
                            continue

                        if (element in sub_box_container):
                            return False
                        sub_box_container.add(element)

                
        return True

