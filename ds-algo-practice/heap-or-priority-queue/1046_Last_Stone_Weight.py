from typing import List
from heapq import heapify, heappop, heappush

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [s * -1 for s in stones]
        heapify(stones)
        heap = stones

        while len(heap) > 1:
            one = heappop(heap)
            two = heappop(heap)
            if one == two:
                continue
            else:
                stone = (one*-1) - (two*-1)
                heappush(heap, stone*-1)
        return heap[0] * -1 if heap else 0
