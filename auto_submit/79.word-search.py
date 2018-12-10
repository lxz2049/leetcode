
# [79] Word Search
#
# https://leetcode.com/problems/word-search/description/
#
# algorithms
# Medium (29.51%)
# Total Accepted:    227.8K
# Total Submissions: 771.7K
# Testcase Example:  '[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]\n"ABCCED"'
#
# Given a 2D board and a word, find if the word exists in the grid.
# 
# The word can be constructed from letters of sequentially adjacent cell, where
# "adjacent" cells are those horizontally or vertically neighboring. The same
# letter cell may not be used more than once.
# 
# Example:
# 
# 
# board =
# [
# ⁠ ['A','B','C','E'],
# ⁠ ['S','F','C','S'],
# ⁠ ['A','D','E','E']
# ]
# 
# Given word = "ABCCED", return true.
# Given word = "SEE", return true.
# Given word = "ABCB", return false.
# 
# 
#
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        visited = [[0] * len(row) for row in board]
        def traverse(i, j, word):
            #print word
            if not word:
                return True
            if i >= 0 and j >= 0 and i < len(board) and j < len(board[i]) and board[i][j] == word[0] and not visited[i][j]:
                visited[i][j] = True
                if any(traverse(x, y, word[1:]) for x, y in ((i+1, j), (i, j+1), (i-1, j), (i, j-1))):
                    return True
                visited[i][j] = False
            return False
        return any(traverse(i, j, word) for i in xrange(len(board)) for j in xrange(len(board[i])))

    def test(self):
        print self.exist([['A','B','C','E'], ['S','F','C','S'], ['A','D','E','E']], "ABCCED")
        print self.exist([['A','B','C','E'], ['S','F','C','S'], ['A','D','E','E']], "SEE")
        print self.exist([['A','B','C','E'], ['S','F','C','S'], ['A','D','E','E']], "ABCB")
