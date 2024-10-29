class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums.sort()
        numSet = set(nums)
        visited = set()
        res = 0
        curr = 0

        for n in nums:
            if n in visited:
                continue
            curr = 0
            while n in numSet:
                n = n ** 2
                curr += 1
            res = max(res, curr)
            visited.add(n)
        return res if res >= 2 else -1