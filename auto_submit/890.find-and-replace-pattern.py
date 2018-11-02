#
# [926] Find and Replace Pattern
#
# https://leetcode.com/problems/find-and-replace-pattern/description/
#
# algorithms
# Medium (68.71%)
# Total Accepted:    11.8K
# Total Submissions: 17.1K
# Testcase Example:  '["abc","deq","mee","aqq","dkd","ccc"]\n"abb"'
#
# You have a list of words and a pattern, and you want to know which words in
# words matches the pattern.
# 
# A word matches the pattern if there exists a permutation of letters p so that
# after replacing every letter x in the pattern with p(x), we get the desired
# word.
# 
# (Recall that a permutation of letters is a bijection from letters to letters:
# every letter maps to another letter, and no two letters map to the same
# letter.)
# 
# Return a list of the words in words that match the given pattern. 
# 
# You may return the answer in any order.
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb"
# Output: ["mee","aqq"]
# Explanation: "mee" matches the pattern because there is a permutation {a ->
# m, b -> e, ...}. 
# "ccc" does not match the pattern because {a -> c, b -> c, ...} is not a
# permutation,
# since a and b map to the same letter.
# 
# 
# 
# Note:
# 
# 
# 1 <= words.length <= 50
# 1 <= pattern.length = words[i].length <= 20
# 
# 
# 
#
class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        def match(a):
            if len(a) != len(pattern):
                return False
            da, db = {}, {}
            for ca, cb in zip(a, pattern):
                if da.get(ca, cb) != cb or db.get(cb, ca) != ca:
                    return False
                da[ca], db[cb] = cb, ca
            return True

        return filter(match, words)

    def test(self):
        print self.findAndReplacePattern(["abc","deq","mee","aqq","dkd","ccc"], "abb")

