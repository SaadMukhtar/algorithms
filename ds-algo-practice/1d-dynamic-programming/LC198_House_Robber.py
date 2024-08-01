class Solution:
    def rob(self, nums: List[int]) -> int:
        DP = [0 for _ in range(len(nums)+2)]
        DP[len(nums)-1] = nums[-1]
        one = 0
        two = 0
        for i in range(len(nums)-2, -1, -1):
            DP[i] = max(nums[i]+DP[i+2], nums[i+1]+DP[i+3])
        return DP[0]
        # @cache
        # def dfs(i):
        #     if i >= len(nums):
        #         return 0
        #     elif i == len(nums) - 1 :
        #         return nums[i]
        #     return max(nums[i]+dfs(i+2), nums[i+1]+dfs(i+3))
        # return dfs(0)