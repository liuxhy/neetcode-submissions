"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        intervals.sort(key=lambda i:i.start)
        free_rooms = []
        heapq.heappush(free_rooms, intervals[0].end)
        for i in range(1, len(intervals)):
            if free_rooms[0] <= intervals[i].start:
                heapq.heappop(free_rooms)
            heapq.heappush(free_rooms, intervals[i].end)

        return len(free_rooms)