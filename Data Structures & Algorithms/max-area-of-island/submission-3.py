class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        directions = [[-1,0],[1,0],[0,1],[0,-1]]
        
        visited = set()
        def dfs(r,c):
            
            

            if r not in range(rows) or c not in range(cols) or grid[r][c] == 0 or (r,c) in visited:
                return 0
            visited.add((r,c))
            temp_sum = 1
            for dr, dc in directions:
                r2 = dr + r
                c2 = dc + c
                temp_sum += dfs(r2,c2)
            
            return temp_sum
        
        res = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in visited:
                    res = max(res, dfs(r,c))
        return res


            

        


