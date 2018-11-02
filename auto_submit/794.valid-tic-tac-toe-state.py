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
            pattern = pp * 3
            for i in xrange(3):
                if board[i*3] == board[i*3 + 1] == board[i*3 + 2] == pp:
                    return True
                if board[i] == board[i + 3] == board[i + 6] == pp:
                    return True
            if board[0] == board[4] == board[8] == pp:
                return True
            if board[2] == board[4] == board[6] == pp:
                return True
            return False
                    
        target = "".join(board)
        target_count = len(target) - target.count(" ")
        visited = set()
        if target.count("X") >= target.count("O"):
            q = deque([("         ", "X", "O", 0)])
            while q:
                board, p, pp, count = q.popleft()
                #print board, p, pp
                if board == target:
                    return True
                if count >= target_count or satisfy(board, pp):
                    continue
                for i, c in enumerate(board):
                    if c == " ":
                        n = board[:i] + p + board[i+1:]
                        if n not in visited:
                            q.append((n, pp, p, count + 1))
                            visited.add(n)

        return False
            

    def test(self):
        print self.validTicTacToe(["O  ", "   ", "   "])
        print self.validTicTacToe(["XOX", " X ", "   "])
        print self.validTicTacToe(["XXX", "   ", "OOO"])
        print self.validTicTacToe(["XOX", "O O", "XOX"])
        print self.validTicTacToe(["OXX", 
                                   "XOX",
                                   "OXO"])
