class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        rows = len(grid)
        cols = len(grid[0])

        moves = [(0,1), (0,-1), (1,0), (-1,0)]

        visit = set()

        def bfs(r,c):

            queue = deque()

            queue.append((r,c))
            res = 1
            visit.add((r,c))

            while queue:

                row, col = queue.popleft()
                
                for nei in moves:

                    newR = row + nei[0]
                    newC = col + nei[1]

                    if newR not in range(rows) or newC not in range(cols) or grid[newR][newC] != 1 or (newR, newC) in visit:
                        continue

                    queue.append((newR, newC))
                    visit.add((newR, newC))
                    res += 1
            return res


        final = 0
        for i in range(rows):
            for j in range(cols):

                if grid[i][j] == 1 and (i,j) not in visit:
                    final = max(final, bfs(i, j))
        return final









            

        


