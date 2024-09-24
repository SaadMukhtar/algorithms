class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.dp = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                leftArea = self.dp[r][c-1] if c > 0 else 0
                rightArea = self.dp[r-1][c] if r > 0 else 0
                overlapArea = self.dp[r-1][c-1] if r > 0 and c > 0 else 0
                self.dp[r][c] = matrix[r][c] + leftArea + rightArea - overlapArea

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        leftArea = self.dp[row1-1][col2] if row1 > 0 else 0 
        topArea = self.dp[row2][col1-1] if col1 > 0 else 0
        overlap = self.dp[row1-1][col1-1] if row1 > 0 and col1 > 0 else 0
        ans = self.dp[row2][col2] - leftArea - topArea + overlap
        return ans
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)