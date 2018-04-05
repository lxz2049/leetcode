#
# [71] Simplify Path
#
# https://leetcode.com/problems/simplify-path/description/
#
# algorithms
# Medium (26.27%)
# Total Accepted:    110.9K
# Total Submissions: 422.1K
# Testcase Example:  '"/"'
#
# Given an absolute path for a file (Unix-style), simplify it.
# 
# For example,
# path = "/home/", => "/home"
# path = "/a/./b/../../c/", => "/c"
# 
# 
# click to show corner cases.
# 
# Corner Cases:
# 
# 
# 
# Did you consider the case where path = "/../"?
# In this case, you should return "/".
# Another corner case is the path might contain multiple slashes '/' together,
# such as "/home//foo/".
# In this case, you should ignore redundant slashes and return "/home/foo".
# 
# 
#
class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        path_components = []
        for c in path.split('/'):
            if c == "..":
                if path_components:
                    path_components.pop()
            elif c and c != ".":
                path_components.append(c)
        path = ""
        for c in path_components:
            path += "/%s" % c

        return path if path else "/"

    def test(self):
        print self.simplifyPath("/")
        print self.simplifyPath("/../")
        print self.simplifyPath("/.")
        print self.simplifyPath("/home")
        print self.simplifyPath("/home/")
        print self.simplifyPath("/home/./b/../../c")
                
