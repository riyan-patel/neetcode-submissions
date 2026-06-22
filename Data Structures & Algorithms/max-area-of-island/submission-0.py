class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        row = len(grid)
        col = len(grid[0])

        max_area = 0
        temp_area = 0
        visited = set()

        def bfs(r, c):
            nonlocal temp_area
            queue = deque()
            queue.append((r,c))
            directions = [[-1,0], [1,0], [0,-1], [0,1]]

            visited.add((r, c))

            while queue:
                ro, co = queue.pop()

                for dr, dc in directions:
                    tr = ro + dr
                    tc = co + dc

                    if (tr in range(row)) and (tc in range(col)) and (grid[tr][tc] == 1) and (tr, tc) not in visited:
                        temp_area += 1
                        queue.append((tr, tc))
                        visited.add((tr,tc))
                        
                        print(temp_area)
                    
        for r in range(row):
            for c in range(col):
                if (grid[r][c] == 1) and (r,c) not in visited:
                    temp_area += 1
                    bfs(r,c)
                    max_area = max(max_area, temp_area)
                    temp_area = 0

        return max_area



