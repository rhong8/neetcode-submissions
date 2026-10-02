class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS = len(board)
        COLS = len(board[0])

        touching_edge = set()
        edges = set()

        def is_valid(r,c):
            return r in range(ROWS) and c in range(COLS)


        def dfs(r,c):
            print(f"dfs at {r}{c}")
            if not is_valid(r,c):
                return
            
            #terminate if you encounter an X, or encounter a point you've already seen
            if board[r][c] == 'X' or board[r][c] == 'T':
                return
        
            #unseen O, put it in the touching edge set
            touching_edge.add((r,c))
            board[r][c] = 'T'

            dfs(r+1, c)
            dfs(r-1,c)
            dfs(r, c+1)
            dfs(r, c-1)
        
        def boundary(r,c):
            return r == 0 or c == 0 or r == ROWS -1 or c == COLS -1
        print("touching edge: ", touching_edge)
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O' and boundary(r,c):
                    touching_edge.add((r,c))
                    dfs(r,c)
                
        print(ROWS, COLS)
        print(boundary(3,1))
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O' and (r,c) not in touching_edge:
                    board[r][c] = 'X'
                elif board[r][c] == 'T':
                    board[r][c] = 'O'
        
        #print(touching_edge)
        