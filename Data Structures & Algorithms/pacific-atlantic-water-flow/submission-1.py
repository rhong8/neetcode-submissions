class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        atlantic = False
        pacific = False
        
        ROWS = len(heights)
        COLS = len(heights[0])
        seen = set()
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        def valid(r, c):
            return r in range(ROWS) and c in range(COLS) and (r,c) not in seen


        #seen is a set
        def dfs(r, c):
            if not valid(r, c):
                return
            nonlocal atlantic
            nonlocal pacific

            if r == 0 or c == 0:
                pacific = True
                #return
            if r == ROWS - 1 or c == COLS - 1:
                atlantic = True
                #return
            
            seen.add((r,c))
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                if valid(nr, nc) and heights[nr][nc] <= heights[r][c]:
                    dfs(nr, nc)
        
        res = []
        for i in range(ROWS):
            for j in range(COLS):
                seen.clear()
                atlantic = False
                pacific = False

                
                    
                
                dfs(i, j)
            
                if atlantic and pacific:
                    res.append([i,j])

        return res


            