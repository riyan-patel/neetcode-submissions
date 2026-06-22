class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        square = collections.defaultdict(set)


        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val == ".":
                    continue
                
                if  (val in cols[j] or
                    val in rows[i] or
                    val in square[(i // 3, j // 3)]):
                        return False
                
                cols[j].add(val)
                rows[i].add(val)
                square[(i//3,j//3)].add(val)
        return True