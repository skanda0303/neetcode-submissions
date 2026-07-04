class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        prevres = intervals[0][1]
        count = 0
        for i in range(1,len(intervals)):
            if intervals[i][0] < prevres:
                count+=1
                prevres = min(intervals[i][1],prevres)
            else:
                prevres = intervals[i][1]
        return count