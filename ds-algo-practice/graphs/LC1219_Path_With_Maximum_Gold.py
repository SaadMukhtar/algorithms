class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        directions = [[1,0], [0,1], [-1, 0], [0, -1]]

        def dfs(r, c):
            res = 0
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == 0 or (r, c) in visited:
                return res
            res = grid[r][c]
            visited.add((r,c))
            for v, h in directions:
                res = max(res, grid[r][c] + dfs(r+v, c+h))
            visited.remove((r,c))
            return res
    
        ans = 0
        for r in range(ROWS):
            for c in range(COLS):
                visited = set()
                ans = max(ans, dfs(r, c))
        return ans


