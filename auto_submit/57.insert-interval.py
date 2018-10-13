#
# [57] Insert Interval
#
# https://leetcode.com/problems/insert-interval/description/
#
# algorithms
# Hard (29.83%)
# Total Accepted:    145.6K
# Total Submissions: 487.8K
# Testcase Example:  '[[1,3],[6,9]]\n[2,5]'
#
# Given a set of non-overlapping intervals, insert a new interval into the
# intervals (merge if necessary).
# 
# You may assume that the intervals were initially sorted according to their
# start times.
# 
# Example 1:
# 
# 
# Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
# Output: [[1,5],[6,9]]
# 
# 
# Example 2:
# 
# 
# Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# Output: [[1,2],[3,10],[12,16]]
# Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
# 
#
# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e
#class Interval(object):
#    def __init__(self, s=0, e=0):
#        self.start = s
#        self.end = e
#    def __repr__(self):
#        return "%s.%s" % (self.start, self.end)


import bisect
class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        i = next((i for i, interval in enumerate(intervals) 
                 if interval.end >= newInterval.start), len(intervals))
        j = next((i for i, interval in enumerate(intervals) 
                 if interval.start > newInterval.end), len(intervals))
        if i < len(intervals) and intervals[i].start < newInterval.start:
            newInterval.start = intervals[i].start
        if j > 0 and intervals[j-1].end > newInterval.end:
            newInterval.end = intervals[j-1].end
        intervals = intervals[:i] + [newInterval] + intervals[j:]
        return intervals
        
    def test(self):
        class Interval(object):
            def __init__(self, s=0, e=0):
                self.start = s
                self.end = e
            def __repr__(self):
                return "%s.%s" % (self.start, self.end)

        print self.insert([Interval(1,3), Interval(6,9)], Interval(2,5))
        print self.insert([Interval(1,2), Interval(3,5), Interval(6,7), Interval(8, 10), Interval(12,16)], Interval(4,8))
        print self.insert([], Interval(4,8))
