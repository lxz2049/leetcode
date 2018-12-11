#
# [30] Substring with Concatenation of All Words
#
# https://leetcode.com/problems/substring-with-concatenation-of-all-words/description/
#
# algorithms
# Hard (22.45%)
# Total Accepted:    108.8K
# Total Submissions: 484.6K
# Testcase Example:  '"barfoothefoobarman"\n["foo","bar"]'
#
# You are given a string, s, and a list of words, words, that are all of the
# same length. Find all starting indices of substring(s) in s that is a
# concatenation of each word in words exactly once and without any intervening
# characters.
# 
# Example 1:
# 
# 
# Input:
# ⁠ s = "barfoothefoobarman",
# ⁠ words = ["foo","bar"]
# Output: [0,9]
# Explanation: Substrings starting at index 0 and 9 are "barfoor" and "foobar"
# respectively.
# The output order does not matter, returning [9,0] is fine too.
# 
# 
# Example 2:
# 
# 
# Input:
# ⁠ s = "wordgoodstudentgoodword",
# ⁠ words = ["word","student"]
# Output: []
# 
# 
#
from collections import Counter
class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not words:
            return []

        ret = []
        wsize = len(words[0])
        ssize = wsize * len(words)
        for i in xrange(wsize):
            lo = cnt = 0
            wordcount = Counter(words)
            for j in xrange((len(s)-i)/wsize):
                w = s[i+j*wsize:i+(j+1)*wsize]
                wordcount[w] -= 1
                while wordcount[w] < 0:
                    wordcount[s[i+lo*wsize:i+(lo+1)*wsize]] += 1
                    lo += 1
                if j - lo + 1 == ssize/wsize:
                    #print w, wordcount, lo, j
                    ret.append(i+lo*wsize)

        return ret

    def test(self):
        print self.findSubstring("barfoothefoobarman", ["foo","bar"])
        print self.findSubstring("wordgoodstudentgoodword", ["word","student"])
        print self.findSubstring("barfoofoobarthefoobarman", ["bar","foo", "the"])
        print self.findSubstring("foobarfoobar", ["foo","bar"])
