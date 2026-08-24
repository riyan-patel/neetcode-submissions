class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        R = len(matrix)
        C = len(matrix[0])

        t = 0
        b = R - 1

        target_row = -1

        while t <= b:

            mid_row = (t + b) // 2

            if target > matrix[mid_row][-1]:
                t = mid_row + 1
            elif target < matrix[mid_row][0]:
                b = mid_row - 1
            else:
                target_row = mid_row
                break
        
        if target_row == -1:
            return False

        
        l = 0
        r = len(matrix[target_row]) - 1

        while l <= r:

            mid = (l + r) // 2

            if target > matrix[target_row][mid]:
                l = mid + 1
            elif target < matrix[target_row][mid]:
                r = mid - 1
            else:
                return True
        
        return False

            

            


        

        

