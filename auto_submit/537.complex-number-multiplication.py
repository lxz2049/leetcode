#
# [537] Complex Number Multiplication
#
# https://leetcode.com/problems/complex-number-multiplication/description/
#
# algorithms
# Medium (63.81%)
# Total Accepted:    21.4K
# Total Submissions: 33.5K
# Testcase Example:  '"1+1i"\n"1+1i"'
#
# 
# Given two strings representing two complex numbers.
# 
# 
# You need to return a string representing their multiplication. Note i2 = -1
# according to the definition.
# 
# 
# Example 1:
# 
# Input: "1+1i", "1+1i"
# Output: "0+2i"
# Explanation: (1 + i) * (1 + i) = 1 + i2 + 2 * i = 2i, and you need convert it
# to the form of 0+2i.
# 
# 
# 
# Example 2:
# 
# Input: "1+-1i", "1+-1i"
# Output: "0+-2i"
# Explanation: (1 - i) * (1 - i) = 1 + i2 - 2 * i = -2i, and you need convert
# it to the form of 0+-2i.
# 
# 
# 
# Note:
# 
# The input strings will not have extra blank.
# The input strings will be given in the form of a+bi, where the integer a and
# b will both belong to the range of [-100, 100]. And the output should be also
# in this form.
# 
# 
#
import re
class Solution(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        regex = "(-?\d+)\+(-?\d+)i"
        ma = re.search(regex, a)
        a_real = int(ma.group(1))
        a_imaginary = int(ma.group(2))
        mb = re.search(regex, b)
        b_real = int(mb.group(1))
        b_imaginary = int(mb.group(2))

        real = a_real * b_real - a_imaginary * b_imaginary
        imaginary = a_real * b_imaginary + b_real * a_imaginary

        return "%d+%di" % (real, imaginary)


"""
if __name__ == "__main__":
    print Solution().complexNumberMultiply("1+1i", "1+1i")
    print Solution().complexNumberMultiply("1+-1i", "1+-1i")
    print Solution().complexNumberMultiply("78+-76i", "-86+72i")
    """
