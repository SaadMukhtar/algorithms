class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sortedArr = sorted(list(set(arr)))
        indexMap = {}
        for i, n in enumerate(sortedArr):
            if indexMap.get(n, 0) == 0:
                indexMap[n] = i+1
        for i, n in enumerate(arr):
            arr[i] = indexMap[n]
        return arr

        
