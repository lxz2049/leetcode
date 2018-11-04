#
# [187] Repeated DNA Sequences
#
# https://leetcode.com/problems/repeated-dna-sequences/description/
#
# algorithms
# Medium (34.31%)
# Total Accepted:    108.5K
# Total Submissions: 315.7K
# Testcase Example:  '"AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"'
#
# All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T,
# for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to
# identify repeated sequences within the DNA.
# 
# Write a function to find all the 10-letter-long sequences (substrings) that
# occur more than once in a DNA molecule.
# 
# Example:
# 
# 
# Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
# 
# Output: ["AAAAACCCCC", "CCCCCAAAAA"]
# 
# 
#
from collections import Counter
class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        ret = []
        sequences = Counter()
        dnaToSeq = {"A": 0, "C": 1, "G": 2, "T": 3}
        seq = 0
        mask = (1 << 20) - 1
        for i, c in enumerate(s):
            seq = (dnaToSeq[c] + (seq << 2)) & mask
            if i >= 9:
                #print s[i-9:i+1], seq
                if sequences[seq] == 1:
                    ret.append(s[i-9:i+1])
                sequences[seq] += 1
        return ret

    def test(self):
        print self.findRepeatedDnaSequences("AAAAAAAAAAA")
        print self.findRepeatedDnaSequences("AAAAAAAAAAAA")
        print self.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT")
        print self.findRepeatedDnaSequences("AAAAAGGGGGAAAAAGGGGGGAAAAACCCCTTT")
