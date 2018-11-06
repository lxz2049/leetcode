#
# [165] Compare Version Numbers
#
# https://leetcode.com/problems/compare-version-numbers/description/
#
# algorithms
# Medium (21.77%)
# Total Accepted:    115.5K
# Total Submissions: 530.3K
# Testcase Example:  '"0.1"\n"1.1"'
#
# Compare two version numbers version1 and version2.
# If version1 > version2 return 1; if version1 < version2 return -1;otherwise
# return 0.
# 
# You may assume that the version strings are non-empty and contain only digits
# and the . character.
# The . character does not represent a decimal point and is used to separate
# number sequences.
# For instance, 2.5 is not "two and a half" or "half way to version three", it
# is the fifth second-level revision of the second first-level revision.
# 
# Example 1:
# 
# 
# Input: version1 = "0.1", version2 = "1.1"
# Output: -1
# 
# Example 2:
# 
# 
# Input: version1 = "1.0.1", version2 = "1"
# Output: 1
# 
# Example 3:
# 
# 
# Input: version1 = "7.5.2.4", version2 = "7.5.3"
# Output: -1
# 
#
from itertools import izip_longest
class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        version1 = version1.split(".")
        version2 = version2.split(".")
        for v1, v2 in izip_longest(version1, version2, fillvalue=0):
            if int(v1) > int(v2):
                return 1
            if int(v1) < int(v2):
                return -1
        return 0

    def test(self):
        print self.compareVersion("0.1", "1.1")
        print self.compareVersion("1.0.1", "1")
        print self.compareVersion("7.5.2.4", "7.5.3")
        print self.compareVersion("7.5.2.4", "7.5.2.4")
        print self.compareVersion("1.0", "1")
