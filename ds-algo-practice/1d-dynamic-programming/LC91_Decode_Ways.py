class Solution:
    def numDecodings(self, s: str) -> int:
        cache = {}

        def decode(i):
            if i in cache:
                return cache[i]
            if i >= len(s):
                return 1
            elif s[i] == '0':
                return 0
            ways = decode(i+1)
            if i + 1 < len(s):
                possibleNum = s[i:i+2]
                num = int(possibleNum)
                if num <= 26:
                    ways += decode(i+2)
            cache[i] = ways
            return ways
        return decode(0)
