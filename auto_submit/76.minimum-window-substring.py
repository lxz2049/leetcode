#
# [76] Minimum Window Substring
#
# https://leetcode.com/problems/minimum-window-substring/description/
#
# algorithms
# Hard (28.12%)
# Total Accepted:    173.6K
# Total Submissions: 616.4K
# Testcase Example:  '"ADOBECODEBANC"\n"ABC"'
#
# Given a string S and a string T, find the minimum window in S which will
# contain all the characters in T in complexity O(n).
# 
# Example:
# 
# 
# Input: S = "ADOBECODEBANC", T = "ABC"
# Output: "BANC"
# 
# 
# Note:
# 
# 
# If there is no such window in S that covers all characters in T, return the
# empty string "".
# If there is such window, you are guaranteed that there will always be only
# one unique minimum window in S.
# 
# 
#
from collections import Counter
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        counter = Counter(t)
        count = len(counter)
        j = 0
        ret_i = None
        ret_j = None
        for i, c in enumerate(s):
            counter[c] -= 1
            if counter[c] == 0:
                count -= 1
            while j < i and counter[s[j]] < 0:
                counter[s[j]] += 1
                j += 1
            if count == 0:
                if ret_i is None or ret_i - ret_j > i - j:
                    ret_i = i
                    ret_j = j

        return s[ret_j:ret_i+1] if ret_j is not None else ""

    def test(self):
        print self.minWindow("ADOBECODEBANC", "ABC")
        print self.minWindow("aa", "aa")
