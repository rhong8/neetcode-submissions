class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()

        INF = 2147483647
        

        ROWS = len(grid)
        COLS = len(grid[0])
        def valid(r,c):
            return r in range(ROWS) and c in range(COLS) and grid[r][c] != -1 and grid[r][c] == INF


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r,c,0)) #push in a 3 tuple
        

        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        while q:
            #print(q)
            for _ in range(len(q)):
            
                r, c, count = q.popleft()


                    
                
                for dr, dc in directions:
                    new_r, new_c = r + dr, c + dc
                    if not valid(new_r, new_c) or grid[new_r][new_c] == 0:
                        continue
                    
                    grid[new_r][new_c] = count + 1
                    q.append((new_r,new_c,count + 1))
                
        
            