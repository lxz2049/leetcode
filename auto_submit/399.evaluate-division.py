#
# [399] Evaluate Division
#
# https://leetcode.com/problems/evaluate-division/description/
#
# algorithms
# Medium (44.01%)
# Total Accepted:    49.8K
# Total Submissions: 112.7K
# Testcase Example:  '[ ["a","b"],["b","c"] ]\n[2.0,3.0]\n[ ["a","c"],["b","c"],["a","e"],["a","a"],["x","x"] ]'
#
# 
# Equations are given in the format A / B = k, where  A and B are variables
# represented as strings, and k is a real number (floating point number). Given
# some queries, return the answers. If the answer does not exist, return -1.0.
# 
# Example:
# Given  a / b = 2.0, b / c = 3.0. queries are:  a / c = ?,  b / a = ?, a / e =
# ?,  a / a = ?, x / x = ? . return  [6.0, 0.5, -1.0, 1.0, -1.0 ].
# 
# 
# The input is:  vector<pair<string, string>> equations, vector<double>&
# values, vector<pair<string, string>> queries , where equations.size() ==
# values.size(), and the values are positive. This represents the equations.
# Return  vector<double>.
# 
# 
# According to the example above:
# equations = [ ["a", "b"], ["b", "c"] ],
# values = [2.0, 3.0],
# queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]. 
# 
# 
# 
# The input is always valid. You may assume that evaluating the queries will
# result in no division by zero and there is no contradiction.
# 
#
from collections import defaultdict
class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        # create graph
        m = defaultdict(dict)
        for equation, val in zip(equations, values):
            num, denom = equation
            m[num][denom] = val
            m[num][num] = m[denom][denom] = 1.0
            m[denom][num] = 1.0 / val

        ret = []
        visited = set()
        def solve(num, denom, val):
            #print num, denom, val, visited
            for d in m[num]:
                if d == denom:
                    ret.append(val * m[num][d])
                    return True
                if d not in visited:
                    visited.add(d)
                    if solve(d, denom, val * m[num][d]):
                        visited.remove(d)
                        return True
                    visited.remove(d)
            return False

        for num, denom in queries:
            visited.add(num)
            if not solve(num, denom, 1):
                ret.append(-1.0)
            visited.remove(num)
        return ret

    def test(self):
        #print self.calcEquation([["a", "b"], ["b", "c"]], [2.0, 3.0], [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ])
        print self.calcEquation([["x1","x2"],["x2","x3"],["x3","x4"],["x4","x5"]], [3.0,4.0,5.0,6.0], [["x1","x5"],["x5","x2"],["x2","x4"],["x2","x2"],["x2","x9"],["x9","x9"]])

