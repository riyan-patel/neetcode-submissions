class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        directions = [[-1,0],[1,0],[0,-1],[0,1]]

        visited = set()

        def bfs(r,c):
            queue = deque()

            queue.append((r,c))
            visited.add((r,c))

            while queue:
                row, col = queue.popleft()

                for dr, dc in directions:
                    r = dr + row
                    c = dc + col

                    if r not in range(rows) or c not in range(cols) or (r,c) in visited or grid[r][c] == "0":
                        continue
                    
                    queue.append((r,c))
                    visited.add((r,c))

        
        res = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    bfs(r,c)
                    res += 1
        return res


