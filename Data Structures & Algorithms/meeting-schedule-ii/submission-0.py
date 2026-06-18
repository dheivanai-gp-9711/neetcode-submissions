"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        #exactly similar to train problem
        startA=[]
        endA=[]
        for i in range(len(intervals)):
            startA.append(intervals[i].start)
            endA.append(intervals[i].end)
        startA.sort()
        endA.sort()

        i=0
        j=0
        count=0
        maxi=0
        while i<len(startA) and j<len(endA):
            if startA[i] < endA[j]:
                count+=1
                maxi = max(maxi, count)
                i+=1
            else:
                count-=1
                j+=1
        return maxi

