#
# [551] Student Attendance Record I
#
# https://leetcode.com/problems/student-attendance-record-i/description/
#
# algorithms
# Easy (44.69%)
# Total Accepted:    38.1K
# Total Submissions: 84.8K
# Testcase Example:  '"PPALLP"'
#
# You are given a string representing an attendance record for a student. The
# record only contains the following three characters:
# 
# 
# 
# 'A' : Absent. 
# 'L' : Late.
# ⁠'P' : Present. 
# 
# 
# 
# 
# A student could be rewarded if his attendance record doesn't contain more
# than one 'A' (absent) or more than two continuous 'L' (late).    
# 
# You need to return whether the student could be rewarded according to his
# attendance record.
# 
# Example 1:
# 
# Input: "PPALLP"
# Output: True
# 
# 
# 
# Example 2:
# 
# Input: "PPALLL"
# Output: False
# 
# 
# 
# 
# 
#
class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        absent_count = 0
        continuous_late_count = 0
        for record in s:
            if record == 'A':
                absent_count += 1
            if record == 'L':
                continuous_late_count += 1
            else:
                continuous_late_count = 0
            if absent_count > 1 or continuous_late_count > 2:
                return False
        return True
                
