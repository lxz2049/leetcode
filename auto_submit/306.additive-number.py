#
# [306] Additive Number
#
# https://leetcode.com/problems/additive-number/description/
#
# algorithms
# Medium (27.71%)
# Total Accepted:    29.6K
# Total Submissions: 106.9K
# Testcase Example:  '"112358"'
#
# Additive number is a string whose digits can form additive sequence.
# 
# A valid additive sequence should contain at least three numbers. Except for
# the first two numbers, each subsequent number in the sequence must be the sum
# of the preceding two.
# 
# 
# For example:
# "112358" is an additive number because the digits can form an additive
# sequence: 1, 1, 2, 3, 5, 8.
# 1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8
# "199100199" is also an additive number, the additive sequence is: 1, 99, 100,
# 199.
# 1 + 99 = 100, 99 + 100 = 199
# 
# 
# 
# Note: Numbers in the additive sequence cannot have leading zeros, so sequence
# 1, 2, 03 or 1, 02, 3 is invalid.
# 
# 
# Given a string containing only digits '0'-'9', write a function to determine
# if it's an additive number.
# 
# 
# Follow up:
# How would you handle overflow for very large input integers?
# 
# 
# Credits:Special thanks to @jeantimex for adding this problem and creating all
# test cases.
#
class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        max_len = len(num) / 2
        for i in range(1, max_len+1):
            for j in range(1, max_len+1):
                if self.calc(num, i, j):
                    return True
        return False
        
    def calc(self, num, len1, len2):
        start1 = 0
        start2 = len1
        while start2+len2 < len(num):
            num1 = int(num[start1:start1+len1])
            num2 = int(num[start2:start2+len2])
            start3 = start2 + len2
            num3 = num1 + num2
            len3 = len(str(num3))
            ##print num1, num2
            if int(num[start3:start3+len3]) == num3 and \
                (num[start1] != '0' or len1 == 1) and \
                (num[start2] != '0' or len2 == 1) and \
                (num[start3] != '0' or len3 == 1):
                start1 = start2
                len1 = len2
                start2 = start3
                len2 = len3
            else:
                return False
        return start1 > 0

"""
if __name__ == '__main__':
    print Solution().isAdditiveNumber("112358")
    print Solution().isAdditiveNumber("0235813")
    print Solution().isAdditiveNumber("199111992")
    print Solution().isAdditiveNumber("10")
    """
