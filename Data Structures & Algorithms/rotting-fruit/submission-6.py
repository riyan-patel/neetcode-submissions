class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        rows = len(grid)
        cols = len(grid[0])

        direction = [[-1,0], [1,0], [0,-1], [0,1]]

        queue = deque()

        fresh = 0
        mins = 0

        for r in range(rows):
            for c in range(cols):

                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    queue.append((r,c))
        

        while queue and fresh > 0:

            for i in range(len(queue)):

                row, col = queue.popleft()

                for dr, dc in direction:
                    r = dr + row
                    c = dc + col

                    if r not in range(rows) or c not in range(cols) or grid[r][c] == 0 or grid[r][c] == 2:
                        continue
                    
                    grid[r][c] = 2
                    queue.append((r,c))

                    fresh -= 1
            mins += 1
        
        return mins if fresh == 0 else -1




            