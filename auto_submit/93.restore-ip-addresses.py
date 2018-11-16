#
# [93] Restore IP Addresses
#
# https://leetcode.com/problems/restore-ip-addresses/description/
#
# algorithms
# Medium (29.76%)
# Total Accepted:    119.9K
# Total Submissions: 402.5K
# Testcase Example:  '"25525511135"'
#
# Given a string containing only digits, restore it by returning all possible
# valid IP address combinations.
# 
# Example:
# 
# 
# Input: "25525511135"
# Output: ["255.255.11.135", "255.255.111.35"]
# 
# 
#
class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        ret = []
        def traverse(candidate, st, cnt):
            if cnt == 4:
                if st == len(s):
                    ret.append(candidate[:-1])
            else:
                if st < len(s) and int(s[st:st+1]) <= 9:
                    traverse(candidate + s[st:st+1] + '.', st+1, cnt+1)
                if st < len(s) - 1 and 10 <= int(s[st:st+2]) <= 99:
                    traverse(candidate + s[st:st+2] + '.', st+2, cnt+1)
                if st < len(s) - 2 and 100 <= int(s[st:st+3]) <= 255:
                    traverse(candidate + s[st:st+3] + '.', st+3, cnt+1)

        traverse("", 0, 0)
        return ret

    def test(self):
        print self.restoreIpAddresses("25525511135")
        print self.restoreIpAddresses("1111")
