#
# [166] Fraction to Recurring Decimal
#
# https://leetcode.com/problems/fraction-to-recurring-decimal/description/
#
# algorithms
# Medium (18.72%)
# Total Accepted:    77K
# Total Submissions: 410.4K
# Testcase Example:  '1\n2'
#
# Given two integers representing the numerator and denominator of a fraction,
# return the fraction in string format.
# 
# If the fractional part is repeating, enclose the repeating part in
# parentheses.
# 
# Example 1:
# 
# 
# Input: numerator = 1, denominator = 2
# Output: "0.5"
# 
# 
# Example 2:
# 
# 
# Input: numerator = 2, denominator = 1
# Output: "2"
# 
# Example 3:
# 
# 
# Input: numerator = 2, denominator = 3
# Output: "0.(6)"
# 
# 
#
class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        ret = []
        if numerator * denominator < 0:
            ret.append("-")
            numerator, denominator = abs(numerator), abs(denominator)
        
        num = numerator / denominator
        ret.append(str(num))

        rem = numerator % denominator
        if rem:
            ret.append(".")
            div_mapping = {}
            while rem:
                if rem in div_mapping:
                    i = div_mapping[rem]
                    ret.insert(i, "(")
                    ret.append(")")
                    break
                else:
                    div_mapping[rem] = len(ret)
                rem *= 10
                num = rem / denominator
                rem = rem % denominator
                ret.append(str(num))
        return "".join(ret)

    def test(self):
        print self.fractionToDecimal(2, 1)
        print self.fractionToDecimal(1, 2)
        print self.fractionToDecimal(2, 3)
        print self.fractionToDecimal(4, 333)
