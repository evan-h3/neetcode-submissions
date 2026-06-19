"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        minheap = []
        for interval in intervals:
            heapq.heappush(minheap, (interval.start,1))
            heapq.heappush(minheap, (interval.end,0))

        conflicts = 0
        meetings = 0

        while minheap:
            val = heapq.heappop(minheap)

            if val[1] == 1:
                meetings+=1
            else:
                meetings-=1
            conflicts = max(meetings, conflicts)

        
        return conflicts
