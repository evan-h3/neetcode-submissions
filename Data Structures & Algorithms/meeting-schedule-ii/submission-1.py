"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key = lambda x: x.start)
        pq = []
        count = 0
        max_val = 0
        for interval in intervals:
            heapq.heappush(pq, (interval.start, 1))
            heapq.heappush(pq, (interval.end, 0))
        while pq:
            time = heapq.heappop(pq)
            if time[1] == 0:
                count-=1
            else:
                count+=1
                max_val = max(count, max_val)
        
        return max_val