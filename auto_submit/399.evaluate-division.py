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
        parents = range(len(equations) * 2)
        size = [1] * (len(equations) * 2)
        ratio = [1.0] * (len(equations) * 2)
        def find(a):
            if a != parents[a]:
                pp = parents[a]
                parents[a] = find(pp)
                ratio[a] *= ratio[pp]
            return parents[a]
        
        def merge(a, b, r):
            ra = find(a)
            rb = find(b)
            if ra == rb:
                return
            if size[ra] < size[rb]:
                ra, rb = rb, ra
                a, b = b, a
                r = 1.0 / r
            parents[rb] = ra
            ratio[rb] = ratio[a] * r / ratio[b]
            size[ra] += size[rb]

        letters = {}
        i = 0
        for e, v in zip(equations, values):
            a, b = e
            if a not in letters:
                letters[a] = i
                i += 1
            if b not in letters:
                letters[b] = i
                i += 1
            merge(letters[a], letters[b], v)

        ret = []
        for a, b in queries:
            if a not in letters or b not in letters:
                ret.append(-1.0)
                continue
            a = letters[a]
            b = letters[b]
            if find(a) != find(b):
                ret.append(-1.0)
            else:
                ret.append(ratio[b] / ratio[a])
        return ret

    def test(self):
        print self.calcEquation([["a", "b"], ["b", "c"]], [2.0, 3.0], [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ])
        #print self.calcEquation([["x1","x2"],["x2","x3"],["x3","x4"],["x4","x5"]], [3.0,4.0,5.0,6.0], [["x1","x5"],["x5","x2"],["x2","x4"],["x2","x2"],["x2","x9"],["x9","x9"]])

