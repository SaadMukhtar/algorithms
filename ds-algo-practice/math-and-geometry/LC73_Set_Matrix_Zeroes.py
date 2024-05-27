from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rowZero, colZero = False, False
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if r == 0 and matrix[r][c] == 0:
                    rowZero = True
                if c == 0 and matrix[r][c] == 0:
                    colZero = True
                if not (r == 0 and c == 0) and matrix[r][c] == 0:
                    matrix[0][c] = 0
                    matrix[r][0] = 0
        
        for r in range(1, len(matrix)):
            for c in range(1, len(matrix[0])):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0
        
        if rowZero:
            for c in range(len(matrix[0])):
                matrix[0][c] = 0
        if colZero:
            for r in range(len(matrix)):
                matrix[r][0] = 0
                    

        