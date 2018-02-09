#
# [14] Longest Common Prefix
#
# https://leetcode.com/problems/longest-common-prefix/description/
#
# algorithms
# Easy (31.60%)
# Total Accepted:    244.6K
# Total Submissions: 774.1K
# Testcase Example:  '[]'
#
# Write a function to find the longest common prefix string amongst an array of
# strings.
#
#
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        return reduce(self.lcp, strs)

    def lcp(self, str1, str2):
        s1 = min(str1, str2)
        s2 = max(str1, str2)
        for i, c in enumerate(s1):
            if c != s2[i]:
                return s1[:i]

        return s1

    def test(self):
        return self.longestCommonPrefix(['a'])
