class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])

        queue = deque()
        visited = set()

        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append((r,c))
                    visited.add((r,c))

        directions = [[-1,0], [1,0], [0,-1], [0,1]]
        #dist = 0
        while queue:
            row, col = queue.popleft()

            for dr, dc in directions:
                
                r = row + dr
                c = col + dc
                
                
                if r in range(rows) and c in range(cols) and (r,c) not in visited and grid[r][c] != -1:
                    grid[r][c] = grid[row][col] + 1
                    visited.add((r,c))
                    queue.append((r,c))
            
            #dist += 1

                

            

            



