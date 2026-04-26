class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix) - 1
        col= len(matrix[0]) - 1

        lRow = 0
        rRow = row

        while lRow <= rRow:
            mRow = lRow + ((rRow - lRow) // 2)
            lCol = 0
            rCol= col
            targetIsGreater = False

            while lCol <= rCol:
                mCol = lCol + ((rCol - lCol) // 2)
                print(mCol)
                if matrix[mRow][mCol] == target:
                    return True
                elif matrix[mRow][mCol] < target:
                    lCol = mCol + 1
                    targetIsGreater = True
                elif matrix[mRow][mCol] > target:
                    rCol = mCol - 1
                    targetIsGreater = False
            
            if targetIsGreater:
                lRow = mRow + 1
            else:
                rRow = mRow - 1
        
        return False
