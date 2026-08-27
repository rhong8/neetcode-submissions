class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()

        time, fresh = 0,0

        ROWS , COLS =  len(grid), len(grid[0])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append([r,c])

        directions = [[0,1], [0,-1], [1,0], [-1,0]]
        
        def valid(x,y):
            return x in range(ROWS) and y in range(COLS) and grid[x][y] == 1

       
        while q and fresh > 0:

            #executing for the right amount of time
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    row, col = dr + r, dc + c
                    #in bounds and its non-rotten
                    if not valid(row, col):
                        continue
                    grid[row][col] = 2
                    q.append([row,col])
                    fresh -= 1
            time += 1
        
        return time if fresh == 0 else - 1



