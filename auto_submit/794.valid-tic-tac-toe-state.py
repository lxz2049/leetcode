#
# [810] Valid Tic-Tac-Toe State
#
# https://leetcode.com/problems/valid-tic-tac-toe-state/description/
#
# algorithms
# Medium (27.99%)
# Total Accepted:    6.3K
# Total Submissions: 22.4K
# Testcase Example:  '["O  ","   ","   "]'
#
# A Tic-Tac-Toe board is given as a string array board. Return True if and only
# if it is possible to reach this board position during the course of a valid
# tic-tac-toe game.
# 
# The board is a 3 x 3 array, and consists of characters " ", "X", and "O".
# The " " character represents an empty square.
# 
# Here are the rules of Tic-Tac-Toe:
# 
# 
# Players take turns placing characters into empty squares (" ").
# The first player always places "X" characters, while the second player always
# places "O" characters.
# "X" and "O" characters are always placed into empty squares, never filled
# ones.
# The game ends when there are 3 of the same (non-empty) character filling any
# row, column, or diagonal.
# The game also ends if all squares are non-empty.
# No more moves can be played if the game is over.
# 
# 
# 
# Example 1:
# Input: board = ["O  ", "   ", "   "]
# Output: false
# Explanation: The first player always plays "X".
# 
# Example 2:
# Input: board = ["XOX", " X ", "   "]
# Output: false
# Explanation: Players take turns making moves.
# 
# Example 3:
# Input: board = ["XXX", "   ", "OOO"]
# Output: false
# 
# Example 4:
# Input: board = ["XOX", "O O", "XOX"]
# Output: true
# 
# 
# Note:
# 
# 
# board is a length-3 array of strings, where each string board[i] has length
# 3.
# Each board[i][j] is a character in the set {" ", "X", "O"}.
# 
# 
#
from collections import deque
class Solution(object):
    def validTicTacToe(self, board):
        """
        :type board: List[str]
        :rtype: bool
        """
        def satisfy(board, pp):
            count = 0
            for i in xrange(3):
                if board[i*3] == board[i*3 + 1] == board[i*3 + 2] == pp:
                    count += 1
                if board[i] == board[i + 3] == board[i + 6] == pp:
                    count += 1
            if board[0] == board[4] == board[8] == pp:
                count += 1
            if board[2] == board[4] == board[6] == pp:
                count += 1
            return count
                    
        target = "".join(board)
        cross_count = target.count("X")
        circle_count = target.count("O")
        cross_satisfy_count = satisfy(target, "X")
        circle_satisfy_count = satisfy(target, "O")
        #print cross_count, circle_count, cross_satisfy_count, circle_satisfy_count
        if cross_count - circle_count == 0 and cross_satisfy_count == 0 and circle_satisfy_count <= 1:
            return True
        elif cross_count - circle_count == 1 and cross_satisfy_count <= 2 and circle_satisfy_count == 0:
            return True
        return False
            

    def test(self):
        print self.validTicTacToe(["O  ", "   ", "   "])
        print self.validTicTacToe(["XOX", " X ", "   "])
        print self.validTicTacToe(["XXX", "   ", "OOO"])
        print self.validTicTacToe(["XOX", "O O", "XOX"])
        print self.validTicTacToe(["OXX", "XOX", "OXO"])
        print self.validTicTacToe(["XXX", "OOX", "OOX"])
