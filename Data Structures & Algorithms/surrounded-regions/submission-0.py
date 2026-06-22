class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])


        def dfs(r,c):
            queue = deque()
            queue.append((r,c))
            directions = [[-1,0], [1,0],[0,-1], [0,1]]

            while queue:
                row, col = queue.popleft()

                if board[row][col] != 'O': continue
                board[row][col] = "T"

                for dr, dc in directions:
                    r = row + dr
                    c = col + dc

                    if r in range(rows) and c in range(cols) and board[r][c] == 'O':
                        queue.append((r,c))

        for r in range(rows):
            dfs(r,0)
            dfs(r, cols - 1)
        
        for c in range(cols):
            dfs(0, c)
            dfs(rows - 1, c)
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"

        