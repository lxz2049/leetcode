#
# [827] Expressive Words
#
# https://leetcode.com/problems/expressive-words/description/
#
# algorithms
# Medium (34.11%)
# Total Accepted:    2.2K
# Total Submissions: 6.4K
# Testcase Example:  '"heeellooo"\n["hello", "hi", "helo"]'
#
# Sometimes people repeat letters to represent extra feeling, such as "hello"
# -> "heeellooo", "hi" -> "hiiii".  Here, we have groups, of adjacent letters
# that are all the same character, and adjacent characters to the group are
# different.  A group is extended if that group is length 3 or more, so "e" and
# "o" would be extended in the first example, and "i" would be extended in the
# second example.  As another example, the groups of "abbcccaaaa" would be "a",
# "bb", "ccc", and "aaaa"; and "ccc" and "aaaa" are the extended groups of that
# string.
# 
# For some given string S, a query word is stretchy if it can be made to be
# equal to S by extending some groups.  Formally, we are allowed to repeatedly
# choose a group (as defined above) of characters c, and add some number of the
# same character c to it so that the length of the group is 3 or more.  Note
# that we cannot extend a group of size one like "h" to a group of size two
# like "hh" - all extensions must leave the group extended - ie., at least 3
# characters long.
# 
# Given a list of query words, return the number of words that are stretchy. 
# 
# 
# Example:
# Input: 
# S = "heeellooo"
# words = ["hello", "hi", "helo"]
# Output: 1
# Explanation: 
# We can extend "e" and "o" in the word "hello" to get "heeellooo".
# We can't extend "helo" to get "heeellooo" because the group "ll" is not
# extended.
# 
# 
# Notes: 
# 
# 
# 0 <= len(S) <= 100.
# 0 <= len(words) <= 100.
# 0 <= len(words[i]) <= 100.
# S and all words in words consist only of lowercase letters
# 
# 
# 
#
class Solution(object):
    def expressiveWords(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: int
        """
        def getGroup(word):
            prev = None
            counter = 0
            for c in word:
                if prev != c:
                    if prev:
                        yield (prev, counter)
                    counter = 0
                    prev = c
                counter += 1
            yield (c, counter)

        from itertools import izip_longest
        ans = 0
        for w in words:
            success = True
            for ((c1, count1), (c2, count2)) in izip_longest(getGroup(w), getGroup(s), 
                                                             fillvalue=(None, None)):
                if not c1 or (c1 != c2 or count1 > count2 or (count1 < count2 and count2 < 3)):
                    success = False
                    break
            if success:
                ans += 1
        return ans


    def test(self):
        print self.expressiveWords('heeeelloooo', ('hello', 'helo', 'hi'))
