class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()
        neighbours = defaultdict(list)
        for s,e in edges:
            neighbours[s].append(e)
            neighbours[e].append(s)

        def dfs(i):
            if i in visited:
                return
            visited.add(i)
            for n in neighbours[i]:
                dfs(n)
        
        res = 0
        for i in range(n):
            if i in visited:
                continue
            dfs(i)
            res += 1
        return res