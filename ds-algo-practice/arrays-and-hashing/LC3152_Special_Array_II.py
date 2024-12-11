class Solution:
    def isArraySpecial(self, nums: list[int], queries: list[list[int]]) -> list[bool]:
        n = len(nums)
        suffix = [1] * n
        res = []

        # Build suffix array
        parity = nums[0] % 2
        for i in range(1, n):
            if nums[i] % 2 != parity:
                suffix[i] = suffix[i - 1] + 1
            parity = nums[i] % 2

        # Process queries
        for start, end in queries:
            if suffix[end] >= end - start + 1:
                res.append(True)
            else:
                res.append(False)

        return res
