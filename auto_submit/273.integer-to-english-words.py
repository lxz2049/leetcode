#
# [273] Integer to English Words
#
# https://leetcode.com/problems/integer-to-english-words/description/
#
# algorithms
# Hard (23.32%)
# Total Accepted:    80.7K
# Total Submissions: 345.8K
# Testcase Example:  '123'
#
# Convert a non-negative integer to its english words representation. Given
# input is guaranteed to be less than 231 - 1.
# 
# Example 1:
# 
# 
# Input: 123
# Output: "One Hundred Twenty Three"
# 
# 
# Example 2:
# 
# 
# Input: 12345
# Output: "Twelve Thousand Three Hundred Forty Five"
# 
# Example 3:
# 
# 
# Input: 1234567
# Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty
# Seven"
# 
# 
# Example 4:
# 
# 
# Input: 1234567891
# Output: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven
# Thousand Eight Hundred Ninety One"
# 
# 
#
class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if not num:
            return "Zero"

        digits = ["", 
                  "One", "Two", "Three", "Four", "Five", 
                  "Six", "Seven", "Eight", "Nine", "Ten", 
                  "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen",
                  "Sixteen", "Seventeen", "Eighteen", "Nineteen", "Twenty",
                  "Thirty", "Forty", "Fifty", "Sixty", "Seventy", 
                  "Eighty", "Ninety"]

        def helper(num):
            h = num / 100 % 10
            t = num % 100
            ret = []
            if h:
                ret.append(digits[h])
                ret.append("Hundred")
            if 0 < t <= 20:
                ret.append(digits[t])
            elif t > 20:
                ret.append(digits[(num % 100) / 10 + 18])
                if num % 10:
                    ret.append(digits[num%10])
            return ret

        ret = []
        b = helper(num / 1000000000 % 1000)
        if b:
            ret.extend(b)
            ret.append("Billion")
        m = helper(num / 1000000 % 1000)
        if m:
            ret.extend(m)
            ret.append("Million")
        t = helper(num / 1000 % 1000)
        if t:
            ret.extend(t)
            ret.append("Thousand")
        d = helper(num % 1000)
        if d:
            ret.extend(d)
        
        return " ".join(ret)

    def test(self):
        print self.numberToWords(123)
        print self.numberToWords(1234)
        print self.numberToWords(12345)
        print self.numberToWords(123456)
        print self.numberToWords(1234567)
        print self.numberToWords(12345678)
        print self.numberToWords(123456789)
        print self.numberToWords(123456789)
        print self.numberToWords(89)
        print self.numberToWords(78)
