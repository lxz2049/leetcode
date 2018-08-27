#
# [874] Backspace String Compare
#
# https://leetcode.com/problems/backspace-string-compare/description/
#
# algorithms
# Easy (53.13%)
# Total Accepted:    13.7K
# Total Submissions: 31K
# Testcase Example:  '"ab#c"\n"ad#c"'
#
# Given two strings S and T, return if they are equal when both are typed into
# empty text editors. # means a backspace character.
# 
# 
# Example 1:
# 
# 
# Input: S = "ab#c", T = "ad#c"
# Output: true
# Explanation: Both S and T become "ac".
# 
# 
# 
# Example 2:
# 
# 
# Input: S = "ab##", T = "c#d#"
# Output: true
# Explanation: Both S and T become "".
# 
# 
# 
# Example 3:
# 
# 
# Input: S = "a##c", T = "#a#c"
# Output: true
# Explanation: Both S and T become "c".
# 
# 
# 
# Example 4:
# 
# 
# Input: S = "a#c", T = "b"
# Output: false
# Explanation: S becomes "c" while T becomes "b".
# 
# 
# Note:
# 
# 
# 1 <= S.length <= 200
# 1 <= T.length <= 200
# S and T only contain lowercase letters and '#' characters.
# 
# 
# Follow up:
# 
# 
# Can you solve it in O(N) time and O(1) space?
# 
# 
# 
# 
# 
#
import itertools
class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        def iter(s):
            skip = 0
            for c in reversed(s):
                if c == '#':
                    skip += 1
                elif not skip:
                    yield c
                else:
                    skip -= 1
        #print list(itertools.izip_longest(iter(S), iter(T)))
        return all(t[0] == t[1] for t in itertools.izip_longest(iter(S), iter(T)))

    def test(self):
        print self.backspaceCompare('bxj##tw', 'bxj###tw')
        print self.backspaceCompare('nzp#o#g', 'b#nzp#o#g')
