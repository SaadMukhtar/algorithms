class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anaMap = defaultdict(list)
        for s in strs:
            anaMap["".join(sorted(s))].append(s)
        return list(anaMap.values())
    