class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sDict = Counter(s)
        tDict = Counter(t)
        return sDict == tDict
