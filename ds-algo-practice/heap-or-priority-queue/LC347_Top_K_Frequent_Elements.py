class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencyMap = Counter(nums)
        heap = []
        for key, v in frequencyMap.items():
            heapq.heappush(heap, (-v, key))
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res