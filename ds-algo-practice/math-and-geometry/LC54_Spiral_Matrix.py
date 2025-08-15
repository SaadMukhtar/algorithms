class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        t, b, l, r = -1, len(matrix), -1, len(matrix[0])
        res = []

        while l + 1 < r and t + 1 < b:
            for i in range(l+1, r):
                res.append(matrix[t+1][i])
            t += 1
            for i in range(t+1, b):
                res.append(matrix[i][r-1])
            r -= 1
            if l + 1 >= r or t + 1 >= b:
                break
            for i in range(r-1, l, -1):
                res.append(matrix[b-1][i])
            b -= 1
            for i in range(b-1, t, -1):
                res.append(matrix[i][l+1])
            l += 1
        return res
                
