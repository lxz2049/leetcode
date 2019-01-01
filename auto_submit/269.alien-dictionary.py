# LintCode
# 892. Alien Dictionary
# There is a new alien language which uses the latin alphabet. However, the order 
# among letters are unknown to you. You receive a list of non-empty words from the 
# dictionary, where words are sorted lexicographically by the rules of this new 
# language. Derive the order of letters in this language.
#
# Example
# Given the following words in dictionary,
#
# [
#   "wrt",
#   "wrf",
#   "er",
#   "ett",
#   "rftt"
# ]
# The correct order is: "wertf"
#
# Given the following words in dictionary,
#
# [
#   "z",
#   "x"
# ]
# The correct order is: "zx".
#
# Notice
# You may assume all letters are in lowercase.
# You may assume that if a is a prefix of b, then a must appear before b in the 
# given dictionary.
# If the order is invalid, return an empty string.
# There may be multiple valid order of letters, return the smallest in 
# lexicographical order
from collections import defaultdict, Counter
from heapq import *
class Solution:
    """
    @param words: a list of words
    @return: a string which is correct order
    """
    def alienOrder(self, words):
        graph = defaultdict(set)
        indegrees = Counter()
        prev = ""
        for w in words:
            for a in w:
                graph.setdefault(a, set())
                indegrees.setdefault(a, 0)
            for a, b in zip(prev, w):
                if a != b:
                    # a -> b
                    graph[a].add(b)                   
                    indegrees[b] += 1
                    break
            prev = w

        # toposort
        ret = []
        heap = [n for n, c in indegrees.iteritems() if c == 0]
        #print graph, indegrees
        while heap:
            n = heappop(heap)
            for nei in graph[n]:
                indegrees[nei] -= 1
                if indegrees[nei] == 0:
                    heappush(heap, nei)
            ret.append(n)
        
        if len(ret) < len(graph):
            return ""
        return "".join(ret)
        
    def test(self):
        print self.alienOrder(["wrt", "wrf", "er", "ett", "rftt"])
        print self.alienOrder(["z", "x"])
        print self.alienOrder(["y", "z", "x", "z"])
        print self.alienOrder(["zy", "zx"])
