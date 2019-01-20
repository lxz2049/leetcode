#
# [207] Course Schedule
#
# https://leetcode.com/problems/course-schedule/description/
#
# algorithms
# Medium (35.58%)
# Total Accepted:    168.9K
# Total Submissions: 473.2K
# Testcase Example:  '2\n[[1,0]]'
#
# There are a total of n courses you have to take, labeled from 0 to n-1.
# 
# Some courses may have prerequisites, for example to take course 0 you have to
# first take course 1, which is expressed as a pair: [0,1]
# 
# Given the total number of courses and a list of prerequisite pairs, is it
# possible for you to finish all courses?
# 
# Example 1:
# 
# 
# Input: 2, [[1,0]] 
# Output: true
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0. So it is possible.
# 
# Example 2:
# 
# 
# Input: 2, [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0, and to take course 0 you
# should
# also have finished course 1. So it is impossible.
# 
# 
# Note:
# 
# 
# The input prerequisites is a graph represented by a list of edges, not
# adjacency matrices. Read more about how a graph is represented.
# You may assume that there are no duplicate edges in the input prerequisites.
# 
# 
#
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        m = {}
        indegrees = [0] * numCourses
        for i, j in prerequisites:
            m.setdefault(i, set())
            m[i].add(j)
            indegrees[j] += 1
        q = [i for i, d in enumerate(indegrees) if d == 0]
        while q:
            i = q.pop()
            for j in m.get(i, {}):
                indegrees[j] -= 1
                if indegrees[j] == 0:
                    q.append(j)
        return sum(indegrees) == 0

    def test(self):
        print self.canFinish(2, [[1,0]])
        print self.canFinish(2, [[1,0], [0,1]])
