#
# [522] Longest Uncommon Subsequence II
#
# https://leetcode.com/problems/longest-uncommon-subsequence-ii/description/
#
# algorithms
# Medium (32.01%)
# Total Accepted:    11.3K
# Total Submissions: 35.3K
# Testcase Example:  '["aba","cdc","eae"]'
#
# 
# Given a list of strings, you need to find the longest uncommon subsequence
# among them. The longest uncommon subsequence is defined as the longest
# subsequence of one of these strings and this subsequence should not be any
# subsequence of the other strings.
# 
# 
# 
# A subsequence is a sequence that can be derived from one sequence by deleting
# some characters without changing the order of the remaining elements.
# Trivially, any string is a subsequence of itself and an empty string is a
# subsequence of any string.
# 
# 
# 
# The input will be a list of strings, and the output needs to be the length of
# the longest uncommon subsequence. If the longest uncommon subsequence doesn't
# exist, return -1.
# 
# 
# Example 1:
# 
# Input: "aba", "cdc", "eae"
# Output: 3
# 
# 
# 
# Note:
# 
# All the given strings' lengths will not exceed 10.
# The length of the given list will be in the range of [2, 50].
# 
# 
#
import itertools
class Solution(object):
    def findLUSlength(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        def isSub(s1, s2):
            i = 0
            for c in s1:
                while i < len(s2) and s2[i] != c:
                    i += 1
                if i >= len(s2):
                    return False
                i += 1
            return True

        ret = -1
        for i in range(0, len(strs)):
            found = False
            for j in range(0, len(strs)):
                if i != j and isSub(strs[i], strs[j]):
                    found = True
                    break
            if not found:
                ret = max(ret, len(strs[i]))

        return ret

    def test(self):
        print self.findLUSlength(['aba', 'cdc', 'eae'])
        print self.findLUSlength(['aaa', 'aaa', 'aa'])
            
