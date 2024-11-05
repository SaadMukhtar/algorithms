class Solution:
    def minChanges(self, s: str) -> int:
        l = 0
        res = 0
        streak = 1
        for r in range(1, len(s)+1):
            if r < len(s) and s[r] == s[l]:
                streak += 1
                continue
            isEven = (streak % 2) == 0
            if isEven:
                streak = 1
                l = r
                continue
            else:
                l = r + 1
                res += 1
                streak = 0
        return res
