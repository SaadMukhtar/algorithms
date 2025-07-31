class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramMap = defaultdict(list)
        for w in strs:
            sortedW = "".join(sorted(w))
            anagramMap[sortedW].append(w)
        return list(anagramMap.values())