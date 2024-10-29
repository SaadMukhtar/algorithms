class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        cache = {}
        visited = set()
        ROWS, COLS = len(grid), len(grid[0])
        

        def dfs(r, c):
            if (r, c) in cache:
                return cache[(r, c)]
            
            directions = [[-1, 1], [0, 1], [1, 1]]
            maxMoves = 0

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] > grid[r][c]:
                    maxMoves = max(maxMoves, 1 + dfs(nr, nc))
            
            cache[(r, c)] = maxMoves
            return maxMoves
        
        res = 0
        for r in range(ROWS):
            res = max(res, dfs(r, 0))
        return res