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
                if (element in rows[r]
                 or element in cols[c]
                 or element in squares[(int(r/3), int(c/3))]):
                    return False
                
                rows[r].add(element)
                cols[c].add(element)
                squares[(int(r/3),int(c/3))].add(element)
        
        


        return True


