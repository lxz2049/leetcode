#
# [140] Word Break II
#
# https://leetcode.com/problems/word-break-ii/description/
#
# algorithms
# Hard (25.24%)
# Total Accepted:    128.9K
# Total Submissions: 507.1K
# Testcase Example:  '"catsanddog"\n["cat","cats","and","sand","dog"]'
#
# Given a non-empty string s and a dictionary wordDict containing a list of
# non-empty words, add spaces in s to construct a sentence where each word is a
# valid dictionary word. Return all such possible sentences.
# 
# Note:
# 
# 
# The same word in the dictionary may be reused multiple times in the
# segmentation.
# You may assume the dictionary does not contain duplicate words.
# 
# 
# Example 1:
# 
# 
# Input:
# s = "catsanddog"
# wordDict = ["cat", "cats", "and", "sand", "dog"]
# Output:
# [
# "cats and dog",
# "cat sand dog"
# ]
# 
# 
# Example 2:
# 
# 
# Input:
# s = "pineapplepenapple"
# wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
# Output:
# [
# "pine apple pen apple",
# "pineapple pen apple",
# "pine applepen apple"
# ]
# Explanation: Note that you are allowed to reuse a dictionary word.
# 
# 
# Example 3:
# 
# 
# Input:
# s = "catsandog"
# wordDict = ["cats", "dog", "sand", "and", "cat"]
# Output:
# []
# 
#
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        wordDict = set(wordDict)
        dp = [None] * len(s)
        def traverse(i):
            if i < len(s) :
                if dp[i] != None:
                    return dp[i]
                dp[i] = [[s[i:k+1]] + rest 
                        for k in xrange(i, len(s)) if s[i:k+1] in wordDict 
                        for rest in traverse(k+1)]
                return dp[i]
            return [[]]

        ret = [" ".join(w) for w in traverse(0)]
        return ret

    def test(self):
        print self.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"])
        print self.wordBreak("catsanddog", ["cats", "dog", "sand", "and", "cat"])  
            

