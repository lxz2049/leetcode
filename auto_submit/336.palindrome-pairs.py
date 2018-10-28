#
# [336] Palindrome Pairs
#
# https://leetcode.com/problems/palindrome-pairs/description/
#
# algorithms
# Hard (28.18%)
# Total Accepted:    50.1K
# Total Submissions: 176.9K
# Testcase Example:  '["abcd","dcba","lls","s","sssll"]'
#
# Given a list of unique words, find all pairs of distinct indices (i, j) in
# the given list, so that the concatenation of the two words, i.e. words[i] +
# words[j] is a palindrome.
# 
# Example 1:
# 
# 
# 
# Input: ["abcd","dcba","lls","s","sssll"]
# Output: [[0,1],[1,0],[3,2],[2,4]] 
# Explanation: The palindromes are ["dcbaabcd","abcddcba","slls","llssssll"]
# 
# 
# 
# Example 2:
# 
# 
# Input: ["bat","tab","cat"]
# Output: [[0,1],[1,0]] 
# Explanation: The palindromes are ["battab","tabbat"]
# 
# 
# 
#
class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        d = {w:k for k, w in enumerate(words)}
        ret = []
        for k, w in enumerate(words):
            rev = w[::-1]
            for i in xrange(len(w) + 1):
                if w[:i] == rev[len(w)-i:]:
                    j = d.get(rev[:len(w)-i])
                    if j is not None and k != j:
                        #print w[:i], rev[len(w)-i:], rev[:len(w)-i]
                        ret.append([j, k])
            for i in xrange(len(w) - 1, -1, -1):
                if w[i:] == rev[:len(w)-i]:
                    j = d.get(rev[len(w)-i:])
                    if j is not None and k != j:
                        #print w[i:], rev[:len(w)-i], rev[len(w)-i:]
                        ret.append([k, j])
        return ret

    def test(self):
        print self.palindromePairs(["abcd","dcba","lls","s","sssll"])
        print self.palindromePairs(["bat","tab","cat"])
