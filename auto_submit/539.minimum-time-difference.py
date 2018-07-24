#
# [539] Minimum Time Difference
#
# https://leetcode.com/problems/minimum-time-difference/description/
#
# algorithms
# Medium (46.04%)
# Total Accepted:    18.4K
# Total Submissions: 39.9K
# Testcase Example:  '["23:59","00:00"]'
#
# Given a list of 24-hour clock time points in "Hour:Minutes" format, find the
# minimum minutes difference between any two time points in the list. 
# 
# Example 1:
# 
# Input: ["23:59","00:00"]
# Output: 1
# 
# 
# 
# Note:
# 
# The number of time points in the given list is at least 2 and won't exceed
# 20000.
# The input time is legal and ranges from 00:00 to 23:59.
# 
# 
#
class Solution(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        def getSeconds(s):
            h, m = s.split(":")
            return int(h)*60 + int(m)
        timePointsSeconds = sorted([getSeconds(t) for t in timePoints])
        ans = timePointsSeconds[0] - timePointsSeconds[-1] + (24*60)
        for i in range(len(timePointsSeconds)-1):
            ans = min(timePointsSeconds[i+1] - timePointsSeconds[i], ans)
        return ans

    def test(self):
        print self.findMinDifference(["23:50", "14:00", "14:01", "00:00"])

