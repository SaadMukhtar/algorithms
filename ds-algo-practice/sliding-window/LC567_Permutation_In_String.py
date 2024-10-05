class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        freqMap = Counter(s1)
        currMap = { c:0 for c in s1 }
        l, r = 0, 0
        while r < len(s2):
            if s2[r] not in freqMap:
                r += 1
                continue
            currMap[s2[r]] += 1
            while (r-l+1) > len(s1) and l != r:
                if s2[l] in freqMap:
                    currMap[s2[l]] -= 1
                l += 1
            if freqMap == currMap:
                return True
            r += 1
        return False
            
