class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not edges:
            return n == 0 or n == 1
        visited = set()
        neighbours = defaultdict(list)
        for n1, n2 in edges:
            neighbours[n1].append(n2)
            neighbours[n2].append(n1)
        
        def visit(node, prev):
            if node in visited:
                return False
            visited.add(node)
            for ne in neighbours[node]:
                if ne == prev:
                    continue
                tryVisit = visit(ne, node)
                if not tryVisit:
                    return False
            
            return True
        return visit(edges[0][0], None) and len(visited) == n