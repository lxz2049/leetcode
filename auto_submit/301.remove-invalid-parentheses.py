#
# [301] Remove Invalid Parentheses
#
# https://leetcode.com/problems/remove-invalid-parentheses/description/
#
# algorithms
# Hard (36.71%)
# Total Accepted:    96.2K
# Total Submissions: 258K
# Testcase Example:  '"()())()"'
#
# Remove the minimum number of invalid parentheses in order to make the input
# string valid. Return all possible results.
# 
# Note: The input string may contain letters other than the parentheses ( and
# ).
# 
# Example 1:
# 
# 
# Input: "()())()"
# Output: ["()()()", "(())()"]
# 
# 
# Example 2:
# 
# 
# Input: "(a)())()"
# Output: ["(a)()()", "(a())()"]
# 
# 
# Example 3:
# 
# 
# Input: ")("
# Output: [""]
# 
#
class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        ret = []
        def remove(s, left, right, last, start):
            #print s, left, right, start
            count = 0
            candidates = []
            for i in xrange(start, len(s)):
                c = s[i]
                if c == left:
                    count += 1
                elif c == right:
                    count -= 1
                if count < 0:
                    # remove extra right parenthesis
                    for j in xrange(i+1):
                        if s[j] == right and (not j or s[j-1] != s[j]) and j >= last:
                            news = s[:j] + s[j+1:i] + s[max(j+1, i):]
                            remove(news, left, right, j, i)
                    return
            if count == 0:
                if left == ")":
                    s = s[::-1]
                ret.append(s)
            else:
                remove(s[::-1], right, left, 0, 0)
                pass
        remove(s, '(', ')', 0, 0)
        return ret

    def test(self):
        print self.removeInvalidParentheses("()")
        print self.removeInvalidParentheses("(a)())()")
        print self.removeInvalidParentheses(")(")
        print self.removeInvalidParentheses("(()")
        print self.removeInvalidParentheses("(r(()()(")
        print self.removeInvalidParentheses("(((k()(((")
