class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()

        ROWS = len(grid)
        COLS = len(grid[0])
        def valid(r, c):
            return r in range(ROWS) and c in range(COLS) and (r,c) not in visited and grid[r][c] == 1

      
        #returns an int
        def dfs(r, c):
            #print(f"traversing {r}, {c}")
            if not valid(r,c):
                return 0
            visited.add((r,c))

            return 1 + dfs(r+1,c) + dfs(r-1, c) + dfs(r, c+1) + dfs(r, c -1) 
        res = 0

        for i in range(ROWS):
            for j in range(COLS):
                if (i,j) not in visited:
                    temp = dfs(i,j)
                    res = max(res, temp)
        
        return res
