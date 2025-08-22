class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        # 
        ROWS, COLS = len(matrix), len(matrix[0])
        res = []
        for c in range(COLS):
            row = []
            for r in range(ROWS):
                row.append(matrix[r][c])
            res.append(row)
        return res
