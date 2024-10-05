class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0 
        while n:
            hasOne = n & 1
            if hasOne:
                count += 1
            n = n >> 1
        return count
    