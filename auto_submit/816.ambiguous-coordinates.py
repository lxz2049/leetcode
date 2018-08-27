#
# [834] Ambiguous Coordinates
#
# https://leetcode.com/problems/ambiguous-coordinates/description/
#
# algorithms
# Medium (41.49%)
# Total Accepted:    3.9K
# Total Submissions: 9.2K
# Testcase Example:  '"(123)"'
#
# We had some 2-dimensional coordinates, like "(1, 3)" or "(2, 0.5)".  Then, we
# removed all commas, decimal points, and spaces, and ended up with the string
# S.  Return a list of strings representing all possibilities for what our
# original coordinates could have been.
# 
# Our original representation never had extraneous zeroes, so we never started
# with numbers like "00", "0.0", "0.00", "1.0", "001", "00.01", or any other
# number that can be represented with less digits.  Also, a decimal point
# within a number never occurs without at least one digit occuring before it,
# so we never started with numbers like ".1".
# 
# The final answer list can be returned in any order.  Also note that all
# coordinates in the final answer have exactly one space between them
# (occurring after the comma.)
# 
# 
# Example 1:
# Input: "(123)"
# Output: ["(1, 23)", "(12, 3)", "(1.2, 3)", "(1, 2.3)"]
# 
# 
# 
# Example 2:
# Input: "(00011)"
# Output:  ["(0.001, 1)", "(0, 0.011)"]
# Explanation: 
# 0.0, 00, 0001 or 00.01 are not allowed.
# 
# 
# 
# Example 3:
# Input: "(0123)"
# Output: ["(0, 123)", "(0, 12.3)", "(0, 1.23)", "(0.1, 23)", "(0.1, 2.3)",
# "(0.12, 3)"]
# 
# 
# 
# Example 4:
# Input: "(100)"
# Output: [(10, 0)]
# Explanation: 
# 1.0 is not allowed.
# 
# 
# 
# 
# Note: 
# 
# 
# 4 <= S.length <= 12.
# S[0] = "(", S[S.length - 1] = ")", and the other elements in S are digits.
# 
# 
# 
#
import itertools
class Solution(object):
    def ambiguousCoordinates(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        s = s[1:len(s)-1]
        ans = []
        def getinteger(integer):
            if not integer:
                return ""
            if integer == "0" or not integer.startswith("0"):
                return "%s" % integer

        def getdecimal(decimal):
            if not decimal:
                return ""
            if not decimal.endswith("0"):
                return ".%s" % decimal
            
        # left value s[:i+1], right value s[i+1:]
        for i in range(len(s)-1):
            # integer s[:j+1], decimal s[j+1:i+1]
            for j in range(i+1):
                left_integer = getinteger(s[:j+1])
                left_decimal = getdecimal(s[j+1:i+1])
                if not left_integer or left_decimal is None:
                    continue
                # integer s[i:k+1], decimal s[k+1:]
                for k in range(i+1, len(s)):
                    right_integer = getinteger(s[i+1:k+1])
                    right_decimal = getdecimal(s[k+1:])
                    if not right_integer or right_decimal is None:
                        continue
                    ans.append("(%s, %s)" % (left_integer + left_decimal, right_integer + right_decimal))

        return ans

    def test(self):
        print self.ambiguousCoordinates("(123)")
        print self.ambiguousCoordinates("(0123)")
        print self.ambiguousCoordinates("(100)")
        print self.ambiguousCoordinates("(00011)")
