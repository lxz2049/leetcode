#
# [211] Add and Search Word - Data structure design
#
# https://leetcode.com/problems/add-and-search-word-data-structure-design/description/
#
# algorithms
# Medium (27.67%)
# Total Accepted:    94.1K
# Total Submissions: 338.8K
# Testcase Example:  '["WordDictionary","addWord","addWord","addWord","search","search","search","search"]\n[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]'
#
# Design a data structure that supports the following two operations:
# 
# 
# void addWord(word)
# bool search(word)
# 
# 
# search(word) can search a literal word or a regular expression string
# containing only letters a-z or .. A . means it can represent any one letter.
# 
# Example:
# 
# 
# addWord("bad")
# addWord("dad")
# addWord("mad")
# search("pad") -> false
# search("bad") -> true
# search(".ad") -> true
# search("b..") -> true
# 
# 
# Note:
# You may assume that all words are consist of lowercase letters a-z.
# 
#
from collections import defaultdict
Trie = lambda: defaultdict(Trie)
class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = Trie()
        

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        node = self.trie
        for c in word:
            node = node[c]
        node.setdefault('_')

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        def traverse(trie, word):
            if not word:
                return '_' in trie
            if word[0] == '.':
                return any(traverse(trie[c], word[1:]) for c in trie if c != '_')
            if word[0] in trie:
                return traverse(trie[word[0]], word[1:])
            return False
        return traverse(self.trie, word)

class Solution:
    def test(self):
        wd = WordDictionary()
        wd.addWord("a")
        wd.addWord("a")
        print wd.search(".")
        print wd.search("a")
        print wd.search("aa")
        print wd.search("a.")
        print wd.search(".a")
        print wd.search("a.")

