class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        i = 0
        nums.sort()

        def twoSum(j, target):
            numMap = {}
            
            while j < len(nums):
                if (target-nums[j]) in numMap:
                    res.append([nums[i], nums[j], target-nums[j]])
                    numMap[nums[j]] = j
                    j += 1
                    while j < len(nums) and nums[j] == nums[j-1]:
                        j += 1
                else:
                    numMap[nums[j]] = j
                    j += 1

        while i < len(nums):
            twoSum(i+1, 0-nums[i])
            i += 1
            while i < len(nums) and nums[i] == nums[i-1]:
                i += 1
        return res