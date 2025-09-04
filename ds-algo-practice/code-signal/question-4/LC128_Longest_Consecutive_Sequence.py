class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        maxStreak = 0
        for n in numSet:
            if (n-1) in numSet:
                continue
            streak = 0
            i = n
            while n in numSet:
                n += 1
                streak += 1
            maxStreak = max(maxStreak, streak)
        return maxStreak