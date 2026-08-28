class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS,  COLS = len(heights), len(heights[0])
        pacific, atlantic = set(), set()


        #can go to squares greater than or equal than the prev
        def dfs(r, c, seen, prevHeight):
            if ((r,c) in seen or (r not in range(ROWS)) or 
            (c not in range(COLS)) or heights[r][c] < prevHeight):
                return
            
            seen.add((r,c))

            dfs(r + 1, c, seen, heights[r][c])
            dfs(r - 1, c, seen, heights[r][c])
            dfs(r, c + 1, seen, heights[r][c])
            dfs(r, c - 1, seen, heights[r][c])

        #outer two rows
        for c in range(COLS):
            dfs(0, c, pacific, 0)
            dfs(ROWS - 1, c, atlantic, 0)
        
        #outer two columns
        for r in range(ROWS):
            dfs(r, 0, pacific, 0)
            dfs(r, COLS - 1, atlantic, 0)

        res = []
        
        for (x, y) in pacific:
            if (x,y) in atlantic:
                res.append([x,y])
        
        return res