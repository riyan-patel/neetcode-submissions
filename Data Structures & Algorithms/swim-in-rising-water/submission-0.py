class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:

        rows = len(grid)
        cols = len(grid[0])
        
        visit = set()

        minH = [[grid[0][0], 0, 0]]

        directions = [[-1,0],[1,0],[0,-1],[0,1]]

        visit.add((0,0))

        while minH:

            t, r, c = heapq.heappop(minH)

            if r == rows - 1 and c == cols - 1:
                return t
            

            for dr, dc in directions:
                row = dr + r
                col = dc + c

                if row not in range(rows) or col not in range(cols) or (row, col) in visit:
                    continue
                
                visit.add((row,col))
                heapq.heappush(minH, [max(t, grid[row][col]), row, col])


