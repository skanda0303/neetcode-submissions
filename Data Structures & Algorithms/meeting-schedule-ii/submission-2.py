class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0

        start = []
        ending = []

        for i in intervals:
            start.append(i.start)
            ending.append(i.end)

        start.sort()
        ending.sort()

        room = 0
        en = 0

        for j in start:
            if j < ending[en]:
                room += 1
            else:
                en += 1

        return room