class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        @cache
        def dfs(i, sum1):
            if sum1 > total // 2 or sum1 < 0:
                return False
            if i == len(nums):
                return sum1 == total / 2
            res = dfs(i+1, sum1+nums[i]) or dfs(i+1, sum1)
            return res
        return dfs(0, 0)
