"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
        def findsort(intervals):
            return intervals.start
        intervals.sort(key=findsort)
        end = intervals[0].end
        for i in range(1,len(intervals)):
            if intervals[i].start < end:
                return False
            end = intervals[i].end
        return True
        
