class Solution:
    def canJump(self, nums: List[int]) -> bool:
        furthest = 0
        for i, n in enumerate(nums):
            if furthest < i:
                return False
            furthest = max(furthest, n+i)
        return True
