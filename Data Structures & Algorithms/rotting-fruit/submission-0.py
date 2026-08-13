class Solution:
        def orangesRotting(self, grid: List[List[int]]) -> int:

            q = collections.deque()

            ROWS = len(grid)
            COLS = len(grid[0])

            for r in range(ROWS):
                for c in range(COLS):
                    if grid[r][c] == 2:
                        q.append((r, c))
            minutes = 0
            


            def valid(x , y):
                return x in range(ROWS) and y in range(COLS) and grid[x][y] == 1
            
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]


            while q:
                layer_size = len(q)
                flag = False
                for _ in range(layer_size):
                    x, y = q.popleft()
    
                    if grid[x][y]:  # super spreader event
                        
                        for dx, dy in directions:
                            nx, ny = x + dx, y + dy
                            if valid(nx, ny): 
                                grid[nx][ny] = 2 #change it to a 2
                                flag = True
                                q.append((nx, ny))
                if flag:
                    minutes += 1
            
            #final sweep:
            for r in range(ROWS):
                for c in range(COLS):
                    if grid[r][c] == 1: #there were some fresh fruits left
                        return -1

            return minutes
