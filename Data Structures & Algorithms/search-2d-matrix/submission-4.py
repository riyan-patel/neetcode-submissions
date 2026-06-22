class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        rows = len(matrix)
        cols = len(matrix[0])


        l = 0
        r = (rows * cols) - 1


        while l <= r:
            mid = (r + l) // 2
            col = mid % cols
            row = mid // cols
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                r = mid - 1
            else:
                l = mid + 1
        return False
            


        

        

