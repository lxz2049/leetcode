#
# [386] Lexicographical Numbers
#
# https://leetcode.com/problems/lexicographical-numbers/description/
#
# algorithms
# Medium (43.59%)
# Total Accepted:    34.2K
# Total Submissions: 78.4K
# Testcase Example:  '13'
#
# 
# Given an integer n, return 1 - n in lexicographical order.
# 
# 
# 
# For example, given 13, return: [1,10,11,12,13,2,3,4,5,6,7,8,9].
# 
# 
# 
# Please optimize your algorithm to use less time and space. The input size may
# be as large as 5,000,000.
# 
#
class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        ret = []
        def traverse(prefix):
            for i in xrange(1 if not prefix else 0, 10):
                m = prefix * 10 + i
                if m <= n:
                    ret.append(m)
                    traverse(m)
                else:
                    return
        traverse(0)
        return ret

    def test(self):
        print self.lexicalOrder(13)
        print self.lexicalOrder(9823)
