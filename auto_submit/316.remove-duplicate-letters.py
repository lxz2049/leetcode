#
# [316] Remove Duplicate Letters
#
# https://leetcode.com/problems/remove-duplicate-letters/description/
#
# algorithms
# Hard (31.02%)
# Total Accepted:    46.6K
# Total Submissions: 150.4K
# Testcase Example:  '"bcabc"'
#
# Given a string which contains only lowercase letters, remove duplicate
# letters so that every letter appear once and only once. You must make sure
# your result is the smallest in lexicographical order among all possible
# results.
# 
# Example 1:
# 
# 
# Input: "bcabc"
# Output: "abc"
# 
# 
# Example 2:
# 
# 
# Input: "cbacdcbc"
# Output: "acdb"
# 
#
from collections import Counter
class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        used = set()
        counter = Counter(s)
        for c in s:
            if c in used:
                counter[c] -= 1
            else:
                while stack and c <= stack[-1] and counter[stack[-1]] > 1:
                    top = stack.pop()
                    counter[top] -= 1
                    used.remove(top)
                stack.append(c)
                used.add(c)
        return "".join(stack)

    def test(self):
        print self.removeDuplicateLetters("cbacdcbc")
        print self.removeDuplicateLetters("bcabc")
        print self.removeDuplicateLetters("dfdeeff")
        print self.removeDuplicateLetters("dfdeeffd")
        print self.removeDuplicateLetters("acabadaea")
        print self.removeDuplicateLetters("bbcaac")
