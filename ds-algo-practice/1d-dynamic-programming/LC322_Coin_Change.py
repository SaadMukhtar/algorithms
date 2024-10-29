class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        @cache
        def dfs(total):
            if total == amount:
                return 0
            elif total > amount:
                return float('inf')
            
            res = float('inf')

            for c in coins:
                res = min(res, 1+dfs(total+c))
            return res
        
        ans = dfs(0)
        if ans >= float('inf'):
            ans = -1
        return ans
