#
# [65] Valid Number
#
# https://leetcode.com/problems/valid-number/description/
#
# algorithms
# Hard (13.47%)
# Total Accepted:    106.3K
# Total Submissions: 788.3K
# Testcase Example:  '"0"'
#
# Validate if a given string can be interpreted as a decimal number.
# 
# Some examples:
# "0" => true
# " 0.1 " => true
# "abc" => false
# "1 a" => false
# "2e10" => true
# " -90e3   " => true
# " 1e" => false
# "e3" => false
# " 6e-1" => true
# " 99e2.5 " => false
# "53.5e93" => true
# " --6 " => false
# "-+3" => false
# "95a54e53" => false
# 
# Note: It is intended for the problem statement to be ambiguous. You should
# gather all requirements up front before implementing one. However, here is a
# list of characters that can be in a valid decimal number:
# 
# 
# Numbers 0-9
# Exponent - "e"
# Positive/negative sign - "+"/"-"
# Decimal point - "."
# 
# 
# Of course, the context of these characters also matters in the input.
# 
# Update (2015-02-10):
# The signature of the C++ function had been updated. If you still see your
# function signature accepts a const char * argument, please click the reload
# button to reset your code definition.
# 
#
class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def isNumber(s, isFloat):
            if s and s[0] in ("+-"):
                s = s[1:]
            if "." in s and isFloat:
                i = s.find(".")
                lo, hi = s[:i], s[i+1:]
                return not lo and hi.isdigit() or not hi and lo.isdigit() or lo.isdigit() and hi.isdigit()
            return s.isdigit()
        s = s.strip()
        if "e" in s:
            i = s.find("e")
            return isNumber(s[:i], True) and isNumber(s[i+1:], False)
        return isNumber(s, True)

    def test(self):
        print self.isNumber("0")
        print self.isNumber(" 0.1 ")
	print self.isNumber("abc")
	print self.isNumber("1 a")
	print self.isNumber("2e10")
	print self.isNumber(" -90e3   ")
	print self.isNumber(" 1e")
	print self.isNumber("e3")
	print self.isNumber(" 6e-1")
	print self.isNumber(" 99e2.5 ")
	print self.isNumber("53.5e93")
	print self.isNumber(" --6 ")
	print self.isNumber("-+3")
	print self.isNumber("95a54e53")
	print self.isNumber(".")
	print self.isNumber(".3")
	print self.isNumber("3.3")
	print self.isNumber("0..")
