class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows = len(grid)
        cols = len(grid[0])

        
        visited = set()


        def bfs(r, c):
            queue = deque()
            visited.add((r,c))
            queue.append((r,c))

            while queue:
                row, col = queue.popleft()
                direction = [[1,0],[-1,0],[0,1],[0,-1]]

                for dr, dc in direction:
                    if ((row + dr) in range(rows)) and ((col + dc) in range(cols)) and (grid[row + dr][col + dc] == "1") and ((row + dr, col + dc) not in visited):
                        queue.append((row + dr, col + dc))
                        visited.add((row + dr, col + dc))
                

        result = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited:

                    bfs(r,c)
                    result += 1
        return result
            
        


