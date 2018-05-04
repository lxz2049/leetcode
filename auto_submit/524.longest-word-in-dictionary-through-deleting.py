#
# [524] Longest Word in Dictionary through Deleting
#
# https://leetcode.com/problems/longest-word-in-dictionary-through-deleting/description/
#
# algorithms
# Medium (43.16%)
# Total Accepted:    22.1K
# Total Submissions: 51.1K
# Testcase Example:  '"abpcplea"\n["ale","apple","monkey","plea"]'
#
# 
# Given a string and a string dictionary, find the longest string in the
# dictionary that can be formed by deleting some characters of the given
# string. If there are more than one possible results, return the longest word
# with the smallest lexicographical order. If there is no possible result,
# return the empty string.
# 
# Example 1:
# 
# Input:
# s = "abpcplea", d = ["ale","apple","monkey","plea"]
# 
# Output: 
# "apple"
# 
# 
# 
# 
# Example 2:
# 
# Input:
# s = "abpcplea", d = ["a","b","c"]
# 
# Output: 
# "a"
# 
# 
# 
# Note:
# 
# All the strings in the input will only contain lower-case letters.
# The size of the dictionary won't exceed 1,000.
# The length of all the strings in the input won't exceed 1,000.
# 
# 
#
class Solution(object):
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        def canReduceInto(s2):
            i = 0
            for c in s2:
                while i < len(s) and s[i] != c:
                    i += 1
                i += 1
            return i <= len(s)
        ans = ""
        for ds in d:
            if canReduceInto(ds):
                #print ds
                if not ans or len(ds) > len(ans) or (len(ds) == len(ans) and ds < ans):
                    ans = ds
                
        return ans

    def test(self):
        print self.findLongestWord('abpcplea', ["ale","apple","monkey","plea"])
        print self.findLongestWord('abpcplea', ["a","b","c","d"])
        print self.findLongestWord('aaa', ["aaa","aa","a"])
