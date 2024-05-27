from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        res = []
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        visited = set()

        def bfs(r, c):
            if r < 0 or c < 0:
                return True, False
            if r >= len(heights) or c >= len(heights[0]):
                return False, True
            pacific, atlantic = False, False
            if (r, c) in visited:
                return False, False
            visited.add((r, c))
            for moveR, moveC in directions:
                newR = r+moveR
                newC = c+moveC
                if newR >= 0 and newR < len(heights) and newC >= 0 and newC < len(heights[0]) and heights[newR][newC] > heights[r][c]:
                    continue
                newPacific, newAtlantic = bfs(newR, newC)
                pacific = pacific or newPacific
                atlantic = atlantic or newAtlantic
                if pacific and atlantic:
                    return True, True
            return pacific, atlantic
        
        for r in range(len(heights)):
            for c in range(len(heights[0])):
                visited = set()
                p, a = bfs(r, c)
                if p and a:
                    res.append([r, c])
        return res
            

             