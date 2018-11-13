#
# [318] Maximum Product of Word Lengths
#
# https://leetcode.com/problems/maximum-product-of-word-lengths/description/
#
# algorithms
# Medium (46.74%)
# Total Accepted:    71K
# Total Submissions: 151.2K
# Testcase Example:  '["abcw","baz","foo","bar","xtfn","abcdef"]'
#
# Given a string array words, find the maximum value of length(word[i]) *
# length(word[j]) where the two words do not share common letters. You may
# assume that each word will contain only lower case letters. If no such two
# words exist, return 0.
# 
# Example 1:
# 
# 
# Input: ["abcw","baz","foo","bar","xtfn","abcdef"]
# Output: 16 
# Explanation: The two words can be "abcw", "xtfn".
# 
# Example 2:
# 
# 
# Input: ["a","ab","abc","d","cd","bcd","abcd"]
# Output: 4 
# Explanation: The two words can be "ab", "cd".
# 
# Example 3:
# 
# 
# Input: ["a","aa","aaa","aaaa"]
# Output: 0 
# Explanation: No such pair of words.
# 
#
class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        def convert(w):
            ret = 0
            for c in w:
                ret |= 1 << (ord(c) - ord('a'))
            return ret
                
        wordlens = [len(w) for w in words]
        words = [convert(w) for w in words]
        try:
            return max((wordlens[i] * wordlens[j] for i in xrange(len(words)) for j in xrange(i) if words[i] & words[j] == 0))
        except:
            return 0

    def test(self):
        print self.maxProduct(["abcw","baz","foo","bar","xtfn","abcdef"])
