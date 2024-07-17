class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counterS = Counter(s)
        counterT = Counter(t)
        if len(counterS) != len(counterT):
            return False

        for k, v in counterS.items():
            if k not in counterT:
                return False
            if v != counterT[k]:
                return False
        return True
            