class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        cache = {}
        def dfs(word):
            if word in cache:
                return cache[word]
            if len(word) == 0:
                return True
            res = False
            for i in range(1, len(word)+1):
                if word[:i] in wordDict:
                    res = dfs(word[i:])
                    if res:
                        break
            cache[word] = res
            return res
        return dfs(s)
