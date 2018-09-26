#
# [833] Bus Routes
#
# https://leetcode.com/problems/bus-routes/description/
#
# algorithms
# Hard (34.03%)
# Total Accepted:    7.7K
# Total Submissions: 22.2K
# Testcase Example:  '[[1,2,7],[3,6,7]]\n1\n6'
#
# We have a list of bus routes. Each routes[i] is a bus route that the i-th bus
# repeats forever. For example if routes[0] = [1, 5, 7], this means that the
# first bus (0-th indexed) travels in the sequence 1->5->7->1->5->7->1->...
# forever.
# 
# We start at bus stop S (initially not on a bus), and we want to go to bus
# stop T. Travelling by buses only, what is the least number of buses we must
# take to reach our destination? Return -1 if it is not possible.
# 
# 
# Example:
# Input: 
# routes = [[1, 2, 7], [3, 6, 7]]
# S = 1
# T = 6
# Output: 2
# Explanation: 
# The best strategy is take the first bus to the bus stop 7, then take the
# second bus to the bus stop 6.
# 
# 
# Note: 
# 
# 
# 1 <= routes.length <= 500.
# 1 <= routes[i].length <= 500.
# 0 <= routes[i][j] < 10 ^ 6.
# 
#
from collections import defaultdict, deque
class Solution(object):
    def numBusesToDestination(self, routes, S, T):
        """
        :type routes: List[List[int]]
        :type S: int
        :type T: int
        :rtype: int
        """
        if S == T:
            return 0

        stops = defaultdict(set)
        for i, route in enumerate(routes):
            for city in route:
                stops[city].add(i)

        visited = defaultdict(bool)
        visitedRoutes = defaultdict(bool)
        queue = deque([(S, 0)])
        visited[S] = True
        while queue:
            city, dist = queue.popleft()
            for stop in stops[city]:
                if not visitedRoutes[stop]:
                    visitedRoutes[stop] = True
                    for neigh in routes[stop]:
                        if neigh == T:
                            return dist + 1
                        if not visited[neigh]:
                            visited[neigh] = True
                            queue.append((neigh, dist+1))
        return -1

    def test(self):
        print self.numBusesToDestination([[1,2,7],[3,6,7]], 1, 6)
                    
