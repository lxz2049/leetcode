#
# [778] Reorganize String
#
# https://leetcode.com/problems/reorganize-string/description/
#
# algorithms
# Medium (39.02%)
# Total Accepted:    15.1K
# Total Submissions: 38.2K
# Testcase Example:  '"aab"'
#
# Given a string S, check if the letters can be rearranged so that two
# characters that are adjacent to each other are not the same.
# 
# If possible, output any possible result.  If not possible, return the empty
# string.
# 
# Example 1:
# 
# 
# Input: S = "aab"
# Output: "aba"
# 
# 
# Example 2:
# 
# 
# Input: S = "aaab"
# Output: ""
# 
# 
# Note:
# 
# 
# S will consist of lowercase letters and have length in range [1, 500].
# 
# 
# 
# 
#
from collections import Counter
class Solution(object):
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        counter = Counter(S)
        last, ret = None, []
        for _ in S:
            try:
                c = max((v, c) for c, v in counter.iteritems() if v and c != last)[1]
            except:
                return ""
            ret.append(c)
            last = c
            counter.subtract(c)
        return "".join(ret)
