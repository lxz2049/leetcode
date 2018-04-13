#
# [134] Gas Station
#
# https://leetcode.com/problems/gas-station/description/
#
# algorithms
# Medium (29.98%)
# Total Accepted:    101.9K
# Total Submissions: 339.9K
# Testcase Example:  '[4]\n[5]'
#
# 
# There are N gas stations along a circular route, where the amount of gas at
# station i is gas[i].
# 
# 
# 
# You have a car with an unlimited gas tank and it costs cost[i] of gas to
# travel from station i to its next station (i+1). You begin the journey with
# an empty tank at one of the gas stations.
# 
# 
# 
# Return the starting gas station's index if you can travel around the circuit
# once, otherwise return -1.
# 
# 
# 
# Note:
# The solution is guaranteed to be unique.
# 
#
class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        remain = 0
        total = 0
        ans = 0
        for i in range(0, len(gas)):
            trip_cost = gas[i] - cost[i]
            total += trip_cost
            remain += trip_cost
            if remain < 0:
                remain = 0
                ans = i+1
        return -1 if total < 0 else ans
            
    def test(self):
        print 0, self.canCompleteCircuit([5, -1, 1, -2, 1, -2], [0, 0, 0, 0, 0, 0])
        print 2, self.canCompleteCircuit([5, -6, 2, -1], [0, 0, 0, 0])
        print -1, self.canCompleteCircuit([5, -5, -1, 0], [0, 0, 0, 0])
        print 3, self.canCompleteCircuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2])


