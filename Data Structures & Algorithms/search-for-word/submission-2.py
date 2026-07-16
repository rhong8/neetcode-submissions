class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        letters = set()
        for letter in word:
            letters.add(letter)
        
        self.exist = False
        ROWS = len(board)
        COLS = len(board[0])
        #set of letters

        def dfs(string, visit, r, c):
            
            if self.exist:
                return
            
            if string == word:
                self.exist = True
                
                return
            
            if r < 0 or c < 0 or r == ROWS or c == COLS or (r,c) in visit or len(string) > len(word) or board[r][c] not in letters:
                return #end that iteration right there
            
            string += board[r][c]
            
            visit.add( (r,c) )
            #explore the four directions
            
            dfs(string, visit, r + 1, c)
            dfs(string, visit, r , c + 1)
            dfs(string, visit, r - 1, c)
            dfs(string, visit, r , c - 1)
            #backtracking step
            visit.remove((r,c))

        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == word[0]:
                    
                    dfs('', set(), r, c)
        


        
        return self.exist