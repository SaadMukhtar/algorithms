import heapq

class Solution:
    def findScore(self, nums: List[int]) -> int:
        marked = set()
        min_heap = []
        res = 0

        for i, n in enumerate(nums):
            heapq.heappush(min_heap, (n, i))

        while min_heap:
            n, i = heapq.heappop(min_heap)
            if i not in marked:
                res += n
                marked.add(i)
                marked.add(i+1)
                marked.add(i-1)
        return res

