#
# [746] Prefix and Suffix Search
#
# https://leetcode.com/problems/prefix-and-suffix-search/description/
#
# algorithms
# Hard (25.85%)
# Total Accepted:    5.9K
# Total Submissions: 22.3K
# Testcase Example:  '["WordFilter","f"]\n[[["apple"]], ["a","e"]]'
#
# 
# Given many words, words[i] has weight i.
# 
# Design a class WordFilter that supports one function, WordFilter.f(String
# prefix, String suffix).
# It will return the word with given prefix and suffix with maximum weight.  If
# no word exists, return -1.
# 
# 
# Examples:
# 
# Input:
# WordFilter(["apple"])
# WordFilter.f("a", "e") // returns 0
# WordFilter.f("b", "") // returns -1
# 
# 
# Note:
# 
# words has length in range [1, 15000].
# For each test case, up to words.length queries WordFilter.f may be made.
# words[i] has length in range [1, 10].
# prefix, suffix have lengths in range [0, 10].
# words[i] and prefix, suffix queries consist of lowercase letters only.
# 
# 
#
import collections
Trie = lambda: collections.defaultdict(Trie)
class WordFilter(object):

    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.trie = Trie()
        self.trie[0] = len(words)-1
        for weight, word in enumerate(words):
            node = self.trie 
            cur = node
            for suffix in reversed(word):
                cur = cur[suffix,]
                cur[0] = weight
            for c in word:
                node = node[c]
                node[0] = weight
                cur = node
                for suffix in reversed(word):
                    cur = cur[suffix,]
                    cur[0] = weight

        
    def f(self, prefix, suffix):
        """
        :type prefix: str
        :type suffix: str
        :rtype: int
        """
        node = self.trie
        for c in prefix:
            node = node[c]

        for c in reversed(suffix):
            node = node[c,]
        return node[0] if 0 in node else -1
    
class Solution():
    @staticmethod
    def print_tree(node, level):
        for k in node:
            if isinstance(node[k], collections.defaultdict):
                print "%s %s" % ("*"*level , k)
                Solution.print_tree(node[k], level+1)

    def test(self):
        f = WordFilter(["apple", "cat"])
        Solution.print_tree(f.trie, 0)
        print f.f("a", "e")
        print f.f("c", "t")
        print f.f("c", "e")
        print f.f("", "")
        print f.f("", "le")
