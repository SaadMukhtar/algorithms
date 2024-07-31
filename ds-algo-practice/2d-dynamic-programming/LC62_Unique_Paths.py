class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        directions = [[1,0], [0, 1]]
        cache = {}
        ROWS = m
        COL = n
        DP = [[0 for _ in range(COL+1)] for _ in range(ROWS+1)]
        DP[m-1][n-1] = 1
        for r in range(ROWS-1, -1, -1):
            for c in range(COL-1, -1, -1):
                if r == m-1 and c == n-1:
                    continue
                count = 0
                for moveR, moveC in directions:
                    count += DP[r+moveR][c+moveC]
                DP[r][c] = count
        return DP[0][0]

        def dfs(r, c):
            if (r, c) in cache:
                return cache[(r, c)]
            if r >= m or c >= n:
                cache[(r, c)] = 0
                return 0
            if r == (m-1) and c == (n-1):
                cache[(r, c)] = 1
                return 1

            count = 0
            for moveR, moveC in directions:
                count += dfs(r+moveR, c+moveC)
            cache[(r, c)] = count
            return count
        return dfs(0, 0)