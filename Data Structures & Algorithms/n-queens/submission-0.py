class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        res = []

        grid = [["."] * n for i in range(n)]

        col = set()
        posdi = set()
        negdi = set()


        def backtrack(r):

            if r == n:

                copy = ["".join(row) for row in grid]
                res.append(copy)
                return
            

            for c in range(n):

                if c in col or (r+c) in posdi or (r-c) in negdi:
                    continue
                
                col.add(c)
                posdi.add(r + c)
                negdi.add(r -c)
                grid[r][c] = "Q"

                backtrack(r + 1)

                col.remove(c)
                posdi.remove(r + c)
                negdi.remove(r - c)
                grid[r][c] = "."
        backtrack(0)

        return res


        