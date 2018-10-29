#
# [424] Longest Repeating Character Replacement
#
# https://leetcode.com/problems/longest-repeating-character-replacement/description/
#
# algorithms
# Medium (42.80%)
# Total Accepted:    22.8K
# Total Submissions: 53.3K
# Testcase Example:  '"ABAB"\n2'
#
# Given a string that consists of only uppercase English letters, you can
# replace any letter in the string with another letter at most k times. Find
# the length of a longest substring containing all repeating letters you can
# get after performing the above operations.
# 
# Note:
# Both the string's length and k will not exceed 104.
# 
# 
# 
# Example 1:
# 
# Input:
# s = "ABAB", k = 2
# 
# Output:
# 4
# 
# Explanation:
# Replace the two 'A's with two 'B's or vice versa.
# 
# 
# 
# 
# Example 2:
# 
# Input:
# s = "AABABBA", k = 1
# 
# Output:
# 4
# 
# Explanation:
# Replace the one 'A' in the middle with 'B' and form "AABBBBA".
# The substring "BBBB" has the longest repeating letters, which is 4.
# 
# 
#
from collections import Counter
class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        counter = Counter()
        ret = i = maxcount = 0
        for j, c in enumerate(s):
            counter[c] += 1
            maxcount = max(maxcount, counter[c])
            if j - i + 1 - maxcount > k:
                counter[s[i]] -= 1
                i += 1
            ret = max(ret, j - i + 1)
        return ret

    def test(self):
        print self.characterReplacement("AABABBA", 1)
        print self.characterReplacement("ABAB", 2)
        print self.characterReplacement("ABBB", 2)
