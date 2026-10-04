class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        visit = set()
        q = deque()

        rows = len(grid)
        cols = len(grid[0])

        INF = 2147483647

        for r in range(rows):
            for c in range(cols):

                if grid[r][c] == 0:
                    q.append((r,c))
                    visit.add((r,c))
        
        moves = [[-1,0], [1,0], [0,1], [0,-1]]
        dist = 0
        while q:

            for i in range(len(q)):
                row, col = q.popleft()

                grid[row][col] = dist

                for dr, dc in moves:
                    r = dr + row
                    c = dc + col

                    if r in range(rows) and c in range(cols) and grid[r][c] != -1 and (r,c) not in visit:
                        q.append((r,c))
                        visit.add((r,c))
            dist += 1


        

                
        






            

            



