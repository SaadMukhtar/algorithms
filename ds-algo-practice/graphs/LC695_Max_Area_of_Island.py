class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        largestIsland = 0
        ROWS, COLS = len(grid), len(grid[0])

        def bfs(r, c):
            q = deque()
            q.append((r, c))
            area = 0
            while q:
                x, y = q.popleft()
                if (x, y) in visited:
                    continue
                visited.add((x, y))
                area += 1
                neighbours = [[1, 0], [0, 1], [-1, 0], [0, -1]]
                for dx, dy in neighbours:
                    nx, ny = x + dx, y + dy
                    if nx not in range(ROWS) or ny not in range(COLS) or grid[nx][ny] != 1:
                        continue
                    q.append((nx, ny))
            return area
        
        for i in range(ROWS):
            for j in range(COLS):
                if (i, j) in visited or grid[i][j] == 0:
                    continue
                largestIsland = max(largestIsland, bfs(i, j))
        return largestIsland
    