class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        fresh = 0
        mins = 0

        queue = deque()


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    queue.append((r,c))
        
        directions = [[-1,0], [1,0], [0,1], [0,-1]]
        while queue and fresh > 0:

            for i in range(len(queue)):
                row, col = queue.popleft()

                for dr, dc in directions:
                    r = row + dr
                    c = col + dc

                    if r not in range(rows) or c not in range(cols) or grid[r][c] != 1:
                        continue
                    grid[r][c] = 2
                    queue.append((r,c))
                    fresh -= 1
            mins += 1
    
        return mins if fresh == 0 else -1
                    




