#
# [395] Longest Substring with At Least K Repeating Characters
#
# https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/description/
#
# algorithms
# Medium (35.92%)
# Total Accepted:    23.2K
# Total Submissions: 64.7K
# Testcase Example:  '"aaabb"\n3'
#
# 
# Find the length of the longest substring T of a given string (consists of
# lowercase letters only) such that every character in T appears no less than k
# times.
# 
# 
# Example 1:
# 
# Input:
# s = "aaabb", k = 3
# 
# Output:
# 3
# 
# The longest substring is "aaa", as 'a' is repeated 3 times.
# 
# 
# 
# Example 2:
# 
# Input:
# s = "ababbc", k = 2
# 
# Output:
# 5
# 
# The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is
# repeated 3 times.
# 
# 
#
import collections
import itertools
class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        def ls(start, end):
            #print start, end
            max_len = 0
            if start >= end:
                return max_len
            j = start
            counter = collections.Counter(itertools.islice(s, start, end))
            for i in xrange(start, end):
                if counter[s[i]] < k:
                    #print s[i], counter[s[i]]
                    max_len = max(max_len, ls(j, i))
                    j = i+1
            if j > start:
                max_len = max(max_len, ls(j, end))
            else:
                max_len = end - start
            return max_len
        
        return ls(0, len(s))

    def test(self):
        print self.longestSubstring("ababbc", 2)
        print self.longestSubstring("aaabb", 3)
