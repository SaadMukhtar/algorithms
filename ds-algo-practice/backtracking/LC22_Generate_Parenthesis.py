class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        visited = set()
        
        def backtrack(open, closed, curr):
            if open == n and closed == n:
                res.append(curr)
                return
            if closed > open or open > n or closed > n:
                return
            backtrack(open+1, closed, curr + "(")
            backtrack(open, closed+1, curr + ")")
        backtrack(0, 0, "")
        return res
