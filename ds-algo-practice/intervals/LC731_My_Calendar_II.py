class MyCalendarTwo:

    def __init__(self):
        self.intervals = []
        

    def book(self, start: int, end: int) -> bool:
        tmpIntervals = self.intervals + [(start, 1), (end, -1)]
        rooms = 0
        res = 0
        tmpIntervals.sort()
        for x, num in tmpIntervals:
            rooms += num
            res = max(res, rooms)
        if res < 3:
            self.intervals += [(start, 1), (end, -1)]
        return res < 3
        


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)