class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        rows = len(grid)
        cols = len(grid[0])

        moves = [(0,1), (0,-1), (1,0), (-1,0)]
        #bfs

        visisted = set()

        def bfs(r, c):
            queue = deque()

            visisted.add((r,c))

            queue.append((r,c))

            while queue:
                currR, currC = queue.popleft()
                for d in moves:
                    newR = currR + d[0]
                    newC = currC + d[1]
                    if newR not in range(rows) or newC not in range(cols) or (newR, newC) in visisted or grid[newR][newC] == "0":
                        continue
                    queue.append((newR, newC))
                    visisted.add((newR, newC))
                
        res = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visisted:
                    bfs(r,c)
                    res += 1
        return res




