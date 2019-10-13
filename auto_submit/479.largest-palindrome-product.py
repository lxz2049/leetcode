#
# @lc app=leetcode id=479 lang=python3
#
# [479] Largest Palindrome Product
#
# https://leetcode.com/problems/largest-palindrome-product/description/
#
# algorithms
# Hard (27.22%)
# Total Accepted:    15.5K
# Total Submissions: 55.6K
# Testcase Example:  '1'
#
# Find the largest palindrome made from the product of two n-digit numbers.
# 
# Since the result could be very large, you should return the largest
# palindrome mod 1337.
# 
# 
# 
# Example:
# 
# Input: 2
# 
# Output: 987
# 
# Explanation: 99 x 91 = 9009, 9009 % 1337 = 987
# 
# 
# 
# Note:
# 
# The range of n is [1,8].
# 
#
class Solution:
    # This is solution is from discussions, not written by me
    def largestPalindrome(self, n: int) -> int:
        if n==1:
            return 9
        high=10**n
        low=10**(n-1)
        for i in range(high-1,low-1,-1):
            w=int(str(i)+str(i)[::-1])
            for i in range(high-1,int(w**0.5)+1,-1):
                #print(w,i)
                if w%i==0:
                    z=w//i
                    if z<high and z>=low:
                        return w%1337

    def test(self):
        for i in range(8):
            print(self.largestPalindrome(i+1))
