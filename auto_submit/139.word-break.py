#
# [139] Word Break
#
# https://leetcode.com/problems/word-break/description/
#
# algorithms
# Medium (32.42%)
# Total Accepted:    250.3K
# Total Submissions: 766.2K
# Testcase Example:  '"leetcode"\n["leet","code"]'
#
# Given a non-empty string s and a dictionary wordDict containing a list of
# non-empty words, determine if s can be segmented into a space-separated
# sequence of one or more dictionary words.
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
# Input: s = "leetcode", wordDict = ["leet", "code"]
# Output: true
# Explanation: Return true because "leetcode" can be segmented as "leet
# code".
# 
# 
# Example 2:
# 
# 
# Input: s = "applepenapple", wordDict = ["apple", "pen"]
# Output: true
# Explanation: Return true because "applepenapple" can be segmented as "apple
# pen apple".
# Note that you are allowed to reuse a dictionary word.
# 
# 
# Example 3:
# 
# 
# Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
# Output: false
# 
# 
#
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        wordDict = set(wordDict)
        dp = [False] * len(s)
        for i in xrange(len(s)):
            if s[:i+1] in wordDict:
                #print s[:i+1]
                dp[i] = True
            else:
                for j in xrange(i):
                    if dp[j] and s[j+1:i+1] in wordDict:
                        #print s[j+1:i+1]
                        dp[i] = True
                        break
        #print dp
        return dp[-1]

    def test(self):
        print self.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"])
        print self.wordBreak("catsanddog", ["cats", "dog", "sand", "and", "cat"])
