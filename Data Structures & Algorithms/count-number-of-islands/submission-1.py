class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()
        islands = 0



        def dfs(x, y):
            if (x in range(ROWS) and y in range(COLS)) and grid[x][y] == '1' and (x,y) not in visited:
                visited.add((x,y))
                dfs(x + 1, y)
                dfs(x, y + 1)
                dfs(x - 1, y)
                dfs(x, y - 1)
                
               
                
            else:
                return

        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1' and (r,c) not in visited:
                    islands += 1
                    dfs(r, c)
        

 
        return islands
