#
# [552] Student Attendance Record II
#
# https://leetcode.com/problems/student-attendance-record-ii/description/
#
# algorithms
# Hard (31.68%)
# Total Accepted:    9K
# Total Submissions: 28.4K
# Testcase Example:  '1'
#
# Given a positive integer n, return the number of all possible attendance
# records with length n, which will be regarded as rewardable. The answer may
# be very large, return it after mod 109 + 7.
# 
# A student attendance record is a string that only contains the following
# three characters:
# 
# 
# 
# 'A' : Absent. 
# 'L' : Late.
# ⁠'P' : Present. 
# 
# 
# 
# 
# A record is regarded as rewardable if it doesn't contain more than one 'A'
# (absent) or more than two continuous 'L' (late).
# 
# Example 1:
# 
# Input: n = 2
# Output: 8 
# Explanation:
# There are 8 records with length 2 will be regarded as rewardable:
# "PP" , "AP", "PA", "LP", "PL", "AL", "LA", "LL"
# Only "AA" won't be regarded as rewardable owing to more than one absent
# times. 
# 
# 
# 
# Note:
# The value of n won't exceed 100,000.
# 
# 
# 
# 
#
class Solution(object):
    def checkRecord(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 3
        zero = 1
        one = 1
        two = 0
        dp = [1] * (n+2)
        mod_constant = 1000000007
        for i in xrange(1, n+1):
            dp[i] = (zero + one + two) % 1000000007
            zero, one, two = (zero + one + two) % 1000000007, zero % 1000000007, one % 1000000007
        ans = 0
        for i in xrange(0, n+1):
            ans += dp[i] * dp[n-1-i]
            ans %= (1000000007)
        return ans

    def test(self):
        print self.checkRecord(2)
        print self.checkRecord(3)
        print self.checkRecord(4)
        print self.checkRecord(5)
        print self.checkRecord(6)
        print self.checkRecord(7)
        print self.checkRecord(100000)

