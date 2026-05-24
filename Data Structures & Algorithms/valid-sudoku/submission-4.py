class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = collections.defaultdict(set)
        cols =  collections.defaultdict(set)
        squares = collections.defaultdict(set) #key = (r/3, c/3)


        for r in range(9):
            for c in range(9):
                element = board[r][c]
                if element == ".":
                    continue
                
                square_key = (r//3, c//3)
                if (element in rows[r]
                 or element in cols[c]
                 or element in squares[square_key]):
                    return False
                
                rows[r].add(element)
                cols[c].add(element)
                squares[square_key].add(element)
        
        

        return True


