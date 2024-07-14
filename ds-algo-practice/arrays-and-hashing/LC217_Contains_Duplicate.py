from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numberSeen = set()
        for n in nums:
            if n in numberSeen:
                return True
            numberSeen.add(n)
        
        return False
        
