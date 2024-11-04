class Solution:
    def compressedString(self, word: str) -> str:
        res = ""
        count = 0
        prev = None
        for c in word:
            if prev == None:
                prev = c
                count += 1
                continue
            if c != prev or count == 9:
                res += f"{count}{prev}"
                prev = c
                count = 1
            else:
                count += 1
        if count:
            res += f"{count}{prev}"
        return res
