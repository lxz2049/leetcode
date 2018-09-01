#
# [130] Surrounded Regions
#
# https://leetcode.com/problems/surrounded-regions/description/
#
# algorithms
# Medium (19.93%)
# Total Accepted:    112.8K
# Total Submissions: 548.9K
# Testcase Example:  '[["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]'
#
# Given a 2D board containing 'X' and 'O' (the letter O), capture all regions
# surrounded by 'X'.
# 
# A region is captured by flipping all 'O's into 'X's in that surrounded
# region.
# 
# Example:
# 
# 
# X X X X
# X O O X
# X X O X
# X O X X
# 
# 
# After running your function, the board should be:
# 
# 
# X X X X
# X X X X
# X X X X
# X O X X
# 
# 
# Explanation:
# 
# Surrounded regions shouldn’t be on the border, which means that any 'O' on
# the border of the board are not flipped to 'X'. Any 'O' that is not on the
# border and it is not connected to an 'O' on the border will be flipped to
# 'X'. Two cells are connected if they are adjacent cells connected
# horizontally or vertically.
# 
#
class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board:
            return

        def traverse(i, j):
            if 0 <= i < len(board) and 0 <= j < len(board[i]) and board[i][j] == 'O':
                    board[i][j] = 'S'
                    traverse(i, j+1)
                    traverse(i, j-1)
                    traverse(i+1, j)
                    traverse(i-1, j)
                    

        for i in xrange(len(board)):
            traverse(i, 0)
            traverse(i, len(board[i])-1)
        for j in xrange(len(board[0])):
            traverse(0, j)
        for j in xrange(len(board[-1])):
            traverse(len(board)-1, j)

        #print board

        for i in xrange(len(board)):
            for j in xrange(len(board[i])):
                if board[i][j] == 'S':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'
                
        #print board

    def test(self):
        self.solve([['X', 'X', 'X', 'X'],
                    ['X', 'O', 'O', 'X'],
                    ['X', 'O', 'O', 'X'],
                    ['X', 'O', 'X', 'X']])

        self.solve([['X', 'X', 'X', 'X'],
                    ['X', 'O', 'O', 'X'],
                    ['X', 'X', 'O', 'X'],
                    ['X', 'O', 'X', 'X']])

        self.solve([['X', 'X', 'X', 'X'],
                    ['X', 'O', 'O', 'X'],
                    ['X', 'O', 'O', 'X'],
                    ['X', 'X', 'X', 'X']])

