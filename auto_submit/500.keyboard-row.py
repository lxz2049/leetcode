#
# [500] Keyboard Row
#
# https://leetcode.com/problems/keyboard-row/description/
#
# algorithms
# Easy (59.75%)
# Total Accepted:    54.7K
# Total Submissions: 91.5K
# Testcase Example:  '["Hello","Alaska","Dad","Peace"]'
#
# Given a List of words, return the words that can be typed using letters of
# alphabet on only one row's of American keyboard like the image below. 
# 
# 
# 
# 
# 
# 
# 
# Example 1:
# 
# Input: ["Hello", "Alaska", "Dad", "Peace"]
# Output: ["Alaska", "Dad"]
# 
# 
# 
# Note:
# 
# You may use one character in the keyboard more than once.
# You may assume the input string will only contain letters of alphabet.
# 
# 
#
class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        upper = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p']
        mid = ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l']
        lower = ['z', 'x', 'c', 'v', 'b', 'n', 'm']
        return [w for w in words if 
                any(map(lambda x: set(list(w.lower())).issubset(x), (upper, mid, lower)))]
