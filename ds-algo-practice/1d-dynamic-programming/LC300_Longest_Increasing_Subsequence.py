class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        LIS = [1] * len(nums)
        for i, n in enumerate(nums):
            for k in range(i):
                if n > nums[k]:
                    LIS[i] = max(LIS[i], 1+LIS[k])
        return max(LIS)
