class Solution:
    def minimumBuckets(self, hamsters: str) -> int:
        res = [0] * len(hamsters)
        for i, c in enumerate(hamsters):
            behindIsFree = False
            if (i-1) >= 0 and hamsters[i-1] != 'H':
                behindIsFree = True
            frontIsFree = False
            if (i+1) < len(hamsters)  and hamsters[i+1] != 'H':
                frontIsFree = True
            if c == 'H' and (((i-1) < 0 or res[i-1] == 0 ) and ((i+1) >= len(hamsters) or res[i+1] == 0)):
                if frontIsFree:
                    res[i+1] = 1
                elif behindIsFree:
                    res[i-1] = 1
                else:
                    return -1

        return sum(res)
