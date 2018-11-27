#
# [793] Swap Adjacent in LR String
#
# https://leetcode.com/problems/swap-adjacent-in-lr-string/description/
#
# algorithms
# Medium (29.87%)
# Total Accepted:    8K
# Total Submissions: 26K
# Testcase Example:  '"X"\n"L"'
#
# In a string composed of 'L', 'R', and 'X' characters, like "RXXLRXRXL", a
# move consists of either replacing one occurrence of "XL" with "LX", or
# replacing one occurrence of "RX" with "XR". Given the starting string start
# and the ending string end, return True if and only if there exists a sequence
# of moves to transform one string to the other.
# 
# Example:
# 
# 
# Input: start = "RXXLRXRXL", end = "XRLXXRRLX"
# Output: True
# Explanation:
# We can transform start to end following these steps:
# RXXLRXRXL ->
# XRXLRXRXL ->
# XRLXRXRXL ->
# XRLXXRRXL ->
# XRLXXRRLX
# 
# 
# Note:
# 
# 
# 1 <= len(start) = len(end) <= 10000.
# Both start and end will only consist of characters in {'L', 'R', 'X'}.
# 
# 
#
class Solution(object):
    def canTransform(self, start, end):
        """
        :type start: str
        :type end: str
        :rtype: bool
        """
        i = j = 0
        l = len(start)
        while i < l or j < l:
            while i < l and start[i] == 'X':
                i += 1
            while j < l and end[j] == 'X':
                j += 1
            if not (i < l and j < l):
                break
            if start[i] != end[j] or i > j and start[i] == 'R' or i < j and start[i] == 'L':
                return False
            i += 1
            j += 1
        return i == j

    def test(self):
        print self.canTransform("RX", "XX")
        print self.canTransform("XXRXLXRXXX", "XXRLXXXXXR")
