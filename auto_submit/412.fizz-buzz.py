#
# [412] Fizz Buzz
#
# https://leetcode.com/problems/fizz-buzz/description/
#
# algorithms
# Easy (58.13%)
# Total Accepted:    117.8K
# Total Submissions: 203.1K
# Testcase Example:  '1'
#
# Write a program that outputs the string representation of numbers from 1 to
# n.
# 
# But for multiples of three it should output “Fizz” instead of the number and
# for the multiples of five output “Buzz”. For numbers which are multiples of
# both three and five output “FizzBuzz”.
# 
# Example:
# 
# n = 15,
# 
# Return:
# [
# ⁠   "1",
# ⁠   "2",
# ⁠   "Fizz",
# ⁠   "4",
# ⁠   "Buzz",
# ⁠   "Fizz",
# ⁠   "7",
# ⁠   "8",
# ⁠   "Fizz",
# ⁠   "Buzz",
# ⁠   "11",
# ⁠   "Fizz",
# ⁠   "13",
# ⁠   "14",
# ⁠   "FizzBuzz"
# ]
# 
# 
#
class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        l = []
        for i in range(n):
            i += 1
            fizzbuzz = ""
            if i % 3 == 0:
                fizzbuzz += "Fizz"
            if i % 5 == 0:
                fizzbuzz += "Buzz"
            if not fizzbuzz:
                fizzbuzz = str(i)
            l.append(fizzbuzz)
        return l
