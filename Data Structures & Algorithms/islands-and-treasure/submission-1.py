class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])
        INF = 2147483647

        directions = [[-1,0], [1,0], [0,1], [0,-1]]
        visited = set()
        queue = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append((r,c))
                    visited.add((r,c))
        
        dist = 0
        while queue:
            for i in range(len(queue)):
                row, col = queue.popleft()
                grid[row][col] = dist
                for dr, dc in directions:
                    r = dr + row
                    c = dc + col
                    if r in range(rows) and c in range(cols) and grid[r][c] != -1 and (r,c) not in visited:
                        queue.append((r,c))
                        visited.add((r,c))
            dist += 1

        

                
        






            

            



