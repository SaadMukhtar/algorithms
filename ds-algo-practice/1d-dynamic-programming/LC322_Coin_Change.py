class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        DP = [amount + 1] * (amount + 1)
        DP[0] = 0
        for i in range(1, amount+1):
            for c in coins:
                if i-c >= 0:
                    DP[i] = min(DP[i-c]+1, DP[i])
        return DP[amount] if DP[amount] != amount+1 else -1


        # @cache
        # def dfs(value):
        #     if value == 0:
        #         return True, 0
        #     if value < 0:
        #         return False, -1
        #     ans = float('inf')
        #     tryCoin = False
        #     for c in coins:
        #         tryCoin, coinsNeeded = dfs(value-c)
        #         if tryCoin:
        #             ans = min(ans, coinsNeeded)
        #     if ans != float('inf'):
        #         return True, ans+1
        #     return False, -1
    
        # return dfs(amount)[1]
        