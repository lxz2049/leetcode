"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param list1: one of the given list
    @param list2: another list
    @return: the new sorted list of interval
    """
    def mergeTwoInterval(self, list1, list2):
        ret = []
        def insertInterval(interval):
            if ret and ret[-1].end >= interval.start:
                ret[-1].end = max(ret[-1].end, interval.end)
            else:
                ret.append(interval)
        
        idx1 = idx2 = 0
        while idx1 < len(list1) or idx2 < len(list2):
            if idx2 >= len(list2) or \
               idx1 < len(list1) and list1[idx1].start < list2[idx2].start:
                insertInterval(list1[idx1])
                idx1 += 1
            else:
                insertInterval(list2[idx2])
                idx2 += 1
            
        return ret

