class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        groups = []
        for i in intervals:
            s, e = i
            groups.append((s, 1))
            groups.append((e, -1))
        
        groups.sort(key=lambda x: (x[0], -x[1]))
        rooms = 0
        maxRooms = 1

        for n, count in groups:
            rooms += count
            maxRooms = max(rooms, maxRooms)
        return maxRooms