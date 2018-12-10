"""
516. Paint House II
There are a row of n houses, each house can be painted with one of the k colors. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color.

The cost of painting each house with a certain color is represented by a n x k cost matrix. For example, costs[0][0] is the cost of painting house 0 with color 0; costs[1][2] is the cost of painting house 1 with color 2, and so on... Find the minimum cost to paint all houses.

Example
Given n = 3, k = 3, costs = [[14,2,11],[11,14,5],[14,3,10]] return 10

house 0 is color 2, house 1 is color 3, house 2 is color 2, 2 + 5 + 3 = 10

Challenge
Could you solve it in O(nk)?

Notice
All costs are positive integers.
"""

class Solution:
    """
    @param costs: n x k cost matrix
    @return: an integer, the minimum cost to paint all houses
    """
    def minCostII(self, costs):
        if not costs:
            return 0
        cur_costs = [0] * len(costs[0])
        for cost in costs:
            min_costs = cur_costs[:]
            for i in xrange(1, len(min_costs)):
                min_costs[i] = min(min_costs[i-1], min_costs[i])
            min_costs_rev = cur_costs[:]
            for i in xrange(len(min_costs)-2, -1, -1):
                min_costs_rev[i] = min(min_costs_rev[i+1], min_costs_rev[i])
            #print cur_costs, min_costs, min_costs_rev
            cur_costs = \
                [c + min(min_costs[i-1] if i else min_costs_rev[i+1], 
                     min_costs_rev[i+1] if i < len(cost) - 1 else min_costs[i-1]) 
        return min(cur_costs)

    def test(self):
        #print self.minCostII([[14,2,11],[11,14,5],[14,3,10]])
        print self.minCostII([[3,5,3],[6,17,6],[7,13,18],[9,10,18]])
