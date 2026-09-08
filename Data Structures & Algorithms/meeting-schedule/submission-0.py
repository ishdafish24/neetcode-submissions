"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        sort_ivls = sorted(intervals, key= lambda x:x.start)
        for i in range(len(sort_ivls)-1):
            if sort_ivls[i].end > sort_ivls[i+1].start:
                return False
        return True
