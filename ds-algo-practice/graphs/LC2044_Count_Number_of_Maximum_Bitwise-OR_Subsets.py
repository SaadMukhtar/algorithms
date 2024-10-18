class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        if not nums:
            return 0
        maxOr = nums[0]
        for n in nums[1:]:
            maxOr |= n
        visited = set()
        res = 0

        def dfs(i, orValue):
            if i >= len(nums):
                return 0
            ans = 0
            if orValue | nums[i] == maxOr:
                ans += 1
            ans += dfs(i+1, orValue|nums[i])
            ans += dfs(i+1, orValue)
            return ans
            

        return dfs(0, 0)
