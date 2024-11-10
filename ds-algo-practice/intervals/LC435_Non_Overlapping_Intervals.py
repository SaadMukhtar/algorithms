class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: (x[0], x[1]))
        curr = intervals[0]
        overlap = 0
        for s, e in intervals[1:]:
            if curr[1] <= s:
                curr = [s, e]
            else:
                overlap += 1
                if e < curr[1]:
                    curr = [s, e]
        return overlap
            