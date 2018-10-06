#
# [420] Strong Password Checker
#
# https://leetcode.com/problems/strong-password-checker/description/
#
# algorithms
# Hard (19.04%)
# Total Accepted:    5.2K
# Total Submissions: 27.8K
# Testcase Example:  '""'
#
# A password is considered strong if below conditions are all met:
# 
# 
# ⁠It has at least 6 characters and at most 20 characters. 
# ⁠It must contain at least one lowercase letter, at least one uppercase
# letter, and at least one digit. 
# ⁠It must NOT contain three repeating characters in a row ("...aaa..." is
# weak, but "...aa...a..." is strong, assuming other conditions are met). 
# 
# 
# Write a function strongPasswordChecker(s), that takes a string s as input,
# and return the MINIMUM change required to make s a strong password. If s is
# already strong, return 0.
# 
# Insertion, deletion or replace of any one character are all considered as one
# change.
#
class Solution(object):
    def strongPasswordChecker(self, s):
        """
        :type s: str
        :rtype: int
        """
        missing_types = 3 - any(c.islower() for c in s) - any(c.isupper() for c in s) - any(c.isdigit() for c in s)
        change = zero = one = two = 0
        last = None
        seqlen = 0
        for c in s:
            if c != last:
                last = c
                if seqlen >= 3:
                    change += seqlen / 3
                    zero += seqlen % 3 == 0
                    one += seqlen % 3 == 1
                seqlen = 1
            else:
                seqlen += 1

        if seqlen >= 3:
            change += seqlen / 3
            zero += seqlen % 3 == 0
            one += seqlen % 3 == 1
        two = change - zero - one

        #print change, zero, one, two
        if len(s) < 6:
            return max(missing_types, 6 - len(s))
        if len(s) <= 20:
            return max(missing_types, change)
        extra = len(s) - 20
        extra, change = extra - min(extra, zero), change - min(extra, zero)
        #print extra, change
        if extra:
            extra, change = extra - min(extra, one * 2), change - min(extra, one * 2) / 2
        #print extra, change
        if extra:
            extra, change = extra - min(extra, two * 3), change - min(extra, two * 3) / 3
        #print extra, change
        return len(s) - 20 + max(missing_types, change)

    def test(self):
        #print self.strongPasswordChecker("aaaaa")
        #print self.strongPasswordChecker("aaaaaaa")
        #print self.strongPasswordChecker("a" * 21)
        #print self.strongPasswordChecker("1234567890123456Baaaaa")
        print self.strongPasswordChecker("10203040aaaaa50607080B")
        print self.strongPasswordChecker("aaaaaa1234567890123Ubefg")

