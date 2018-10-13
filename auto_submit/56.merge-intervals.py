#
# [56] Merge Intervals
#
# https://leetcode.com/problems/merge-intervals/description/
#
# algorithms
# Medium (33.22%)
# Total Accepted:    247.6K
# Total Submissions: 744.7K
# Testcase Example:  '[[1,3],[2,6],[8,10],[15,18]]'
#
# Given a collection of intervals, merge all overlapping intervals.
# 
# Example 1:
# 
# 
# Input: [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into
# [1,6].
# 
# 
# Example 2:
# 
# 
# Input: [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considerred overlapping.
# 
#
# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        intervals.sort(key=lambda x: (x.start, x.end))
        ret = []
        for interval in intervals:
            #print ret[-1] if ret else [], interval
            if ret and ret[-1].start <= interval.start <= ret[-1].end:
                ret[-1].end = max(ret[-1].end, interval.end)
            else:
                ret.append(interval)
        return ret

    def test(self):
        class Interval(object):
            def __init__(self, s=0, e=0):
                self.start = s
                self.end = e
            def __repr__(self):
                return "%s,%s" % (self.start, self.end)

        print self.merge([Interval(1,3), Interval(2,6), Interval(8,10), Interval(15,18)])
        print self.merge([Interval(1,4), Interval(4,5)])
