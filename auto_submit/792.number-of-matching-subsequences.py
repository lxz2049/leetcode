#
# [808] Number of Matching Subsequences
#
# https://leetcode.com/problems/number-of-matching-subsequences/description/
#
# algorithms
# Medium (39.49%)
# Total Accepted:    14.2K
# Total Submissions: 35.7K
# Testcase Example:  '"abcde"\n["a","bb","acd","ace"]'
#
# Given string S and a dictionary of words words, find the number of words[i]
# that is a subsequence of S.
# 
# 
# Example :
# Input: 
# S = "abcde"
# words = ["a", "bb", "acd", "ace"]
# Output: 3
# Explanation: There are three words in words that are a subsequence of S: "a",
# "acd", "ace".
# 
# 
# Note:
# 
# 
# All words in words and S will only consists of lowercase letters.
# The length of S will be in the range of [1, 50000].
# The length of words will be in the range of [1, 5000].
# The length of words[i] will be in the range of [1, 50].
# 
# 
#
from collections import defaultdict
from bisect import bisect_right
class Solution(object):
    def numMatchingSubseq(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        lookup = defaultdict(list)
        for i, c in enumerate(S):
            lookup[c].append(i)
        def check(s):
            i = -1
            for c in s:
                j = bisect_right(lookup[c], i)
                if j < len(lookup[c]):
                    i = lookup[c][j]
                else:
                    return False
            return True
        return sum(1 for w in words if check(w))
