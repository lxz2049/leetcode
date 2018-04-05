#
# [539] Minimum Time Difference
#
# https://leetcode.com/problems/minimum-time-difference/description/
#
# algorithms
# Medium (46.01%)
# Total Accepted:    15.9K
# Total Submissions: 34.5K
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
        def getMin(t):
            h, m = t.split(':')
            return int(h) * 60 + int(m)
        
        timePoints.sort(key=getMin)
        ans = getMin(timePoints[0]) + 24*60 - getMin(timePoints[-1])
        for i in range(0, len(timePoints)-1):
            ans = min(ans, getMin(timePoints[i+1]) - getMin(timePoints[i]))
            
        return ans

    def test(self):
        print self.findMinDifference(["23:59", "00:00"])


            
