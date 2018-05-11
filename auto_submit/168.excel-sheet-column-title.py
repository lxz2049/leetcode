#
# [168] Excel Sheet Column Title
#
# https://leetcode.com/problems/excel-sheet-column-title/description/
#
# algorithms
# Easy (27.26%)
# Total Accepted:    136.3K
# Total Submissions: 497.3K
# Testcase Example:  '1'
#
# Given a positive integer, return its corresponding column title as appear in
# an Excel sheet.
# 
# For example:
# 
# 
# ⁠   1 -> A
# ⁠   2 -> B
# ⁠   3 -> C
# ⁠   ...
# ⁠   26 -> Z
# ⁠   27 -> AA
# ⁠   28 -> AB 
# ⁠   ...
# 
# 
# Example 1:
# 
# 
# Input: 1
# Output: "A"
# 
# 
# Example 2:
# 
# 
# Input: 28
# Output: "AB"
# 
# 
# Example 3:
# 
# 
# Input: 701
# Output: "ZY"
# 
# 
#
class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        charactermap = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        ret = []
        while n > 0:
            n -= 1
            #print n%26, n/26
            ret += charactermap[n % 26]
            n /= 26
        return "".join(reversed(ret))


    def test(self):
        print self.convertToTitle(1)
        print self.convertToTitle(28)
        print self.convertToTitle(701)
        print self.convertToTitle(702)
        print self.convertToTitle(703)
