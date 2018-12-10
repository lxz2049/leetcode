#
# [212] Word Search II
#
# https://leetcode.com/problems/word-search-ii/description/
#
# algorithms
# Hard (26.58%)
# Total Accepted:    87.7K
# Total Submissions: 330K
# Testcase Example:  '[["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]\n["oath","pea","eat","rain"]'
#
# Given a 2D board and a list of words from the dictionary, find all words in
# the board.
# 
# Each word must be constructed from letters of sequentially adjacent cell,
# where "adjacent" cells are those horizontally or vertically neighboring. The
# same letter cell may not be used more than once in a word.
# 
# Example:
# 
# 
# Input: 
# words = ["oath","pea","eat","rain"] and board =
# [
# ⁠ ['o','a','a','n'],
# ⁠ ['e','t','a','e'],
# ⁠ ['i','h','k','r'],
# ⁠ ['i','f','l','v']
# ]
# 
# Output: ["eat","oath"]
# 
# 
# Note:
# You may assume that all inputs are consist of lowercase letters a-z.
#
from collections import defaultdict
Trie = lambda: defaultdict(Trie)

class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        trie = Trie()
        def addword(word):
            node = trie
            for c in word:
                node = node[c]
            node["_"] = word
        for w in words:
            addword(w)

        ret = set()
        visited = [[0] * len(row) for row in board]
        def traverse(i, j, node):
            if "_" in node:
                ret.add(node["_"])               
            c = board[i][j]
            visited[i][j] = True
            for x, y in ((i+1, j), (i, j+1), (i-1, j), (i, j-1)):
                if x >= 0 and y >= 0 and x < len(board) and y < len(board[x]) and \
                   board[x][y] in node and not visited[x][y]:
                    traverse(x, y, node[board[x][y]]) 
            visited[i][j] = False

        for i in xrange(len(board)):
            for j in xrange(len(board[i])):
                if board[i][j] in trie:
                    traverse(i, j, trie[board[i][j]])
        return list(ret)

    def test(self):
        print self.findWords([['o','a','a','n'],
                              ['e','t','a','e'],
                              ['i','h','k','r'],
                              ['i','f','l','v']],
                              ["oath","pea","eat","rain"])
