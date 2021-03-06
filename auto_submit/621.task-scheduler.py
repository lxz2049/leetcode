#
# [621] Task Scheduler
#
# https://leetcode.com/problems/task-scheduler/description/
#
# algorithms
# Medium (42.95%)
# Total Accepted:    57.2K
# Total Submissions: 133.1K
# Testcase Example:  '["A","A","A","B","B","B"]\n2'
#
# Given a char array representing tasks CPU need to do. It contains capital
# letters A to Z where different letters represent different tasks.Tasks could
# be done without original order. Each task could be done in one interval. For
# each interval, CPU could finish one task or just be idle.
# 
# However, there is a non-negative cooling interval n that means between two
# same tasks, there must be at least n intervals that CPU are doing different
# tasks or just be idle.
# 
# You need to return the least number of intervals the CPU will take to finish
# all the given tasks.
# 
# 
# 
# Example:
# 
# 
# Input: tasks = ["A","A","A","B","B","B"], n = 2
# Output: 8
# Explanation: A -> B -> idle -> A -> B -> idle -> A -> B.
# 
# 
# 
# 
# Note:
# 
# 
# The number of tasks is in the range [1, 10000].
# The integer n is in the range [0, 100].
# 
# 
#
from collections import Counter, defaultdict
class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        taskCounter = Counter(tasks)
        taskCountCounter = Counter(taskCounter[t] for t in taskCounter)
        maxTaskCount = max(taskCountCounter)
        maxCountTaskCount = taskCountCounter[maxTaskCount]
        return max(len(tasks), (maxTaskCount - 1) * (n + 1) + maxCountTaskCount)

    def test(self):
        print self.leastInterval(["A","A","A","B","B","B"], 2)
        print self.leastInterval(["A","B","B","B"], 2)
