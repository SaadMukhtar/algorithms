class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        Dp[l][r] = 0 if l >= len(text1) or r >= len(text2)
        Dp[l][r] = Dp[l+1][r+1] if text1[l] == text2[r]
        Dp[l][r] = max(Dp[l+1, r], Dp[l, r+1]) if text1[l] != text2[r]
        """
        ROWS = len(text1) + 1
        COL = len(text2) + 1
        Dp = [[0 for _ in range(COL)] for _ in range(ROWS)]
        for l in range(len(text1)-1, -1, -1):
            for r in range(len(text2)-1, -1, -1):
                if text1[l] == text2[r]:
                    Dp[l][r] = 1 + Dp[l+1][r+1]
                else:
                    Dp[l][r] = max(Dp[l+1][r], Dp[l][r+1])
        return Dp[0][0]

        # DFS Version
        # @cache
        # def dfs(l, r):
        #     if l >= len(text1):
        #         return 0
        #     if r >= len(text2):
        #         return 0
        #     res = 0
        #     other = 0
        #     if text1[l] == text2[r]:
        #         res = 1 + dfs(l+1, r+1)
        #     else:
        #         res = max(dfs(l+1, r), dfs(l, r+1))
        #     return res
        # return dfs(0, 0)
