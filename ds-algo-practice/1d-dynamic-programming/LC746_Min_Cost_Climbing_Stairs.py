class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        ans = (len(cost)+2) * [0]
        ans[-1] = 0
        for i in range(len(cost)-1, -1, -1):
            ans[i] = cost[i] + min(ans[i+1], ans[i+2])
        return min(ans[0], ans[1])
        # @cache
        # def dfs(i):
        #     if i == len(cost):
        #         return 0
        #     elif i > len(cost):
        #         return float('inf')
        #     return cost[i] + min(dfs(i+1), dfs(i+2))

        # return min(dfs(0), dfs(1))