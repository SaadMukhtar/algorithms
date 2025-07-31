class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        duplicateMap = {}
        for n in nums:
            if n in duplicateMap:
                return True
            duplicateMap[n] = True
        return False