/*
 * [58] Length of Last Word
 *
 * https://leetcode.com/problems/length-of-last-word/description/
 *
 * algorithms
 * Easy (32.05%)
 * Total Accepted:    177.3K
 * Total Submissions: 553.2K
 * Testcase Example:  '"Hello World"'
 *
 * Given a string s consists of upper/lower-case alphabets and empty space
 * characters ' ', return the length of last word in the string.
 * 
 * If the last word does not exist, return 0.
 * 
 * Note: A word is defined as a character sequence consists of non-space
 * characters only.
 * 
 * Example:
 * 
 * Input: "Hello World"
 * Output: 5
 * 
 * 
 */
class Solution {
public:
    int lengthOfLastWord(string s) {
		int len = s.length();
		int i = len-1;
		while (i>=0 && s[i] == ' ') {
			i--;
			len--;
		}
 		while (i>=0 && s[i] != ' ') {
			i--;
		}
		return len-i-1;
    }
};
