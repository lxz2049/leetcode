/*
 * [151] Reverse Words in a String
 *
 * https://leetcode.com/problems/reverse-words-in-a-string/description/
 *
 * algorithms
 * Medium (15.73%)
 * Total Accepted:    234.1K
 * Total Submissions: 1.5M
 * Testcase Example:  '"the sky is blue"'
 *
 * Given an input string, reverse the string word by word.
 * 
 * Example:  
 * 
 * 
 * Input: "the sky is blue",
 * Output: "blue is sky the".
 * 
 * 
 * Note:
 * 
 * 
 * A word is defined as a sequence of non-space characters.
 * Input string may contain leading or trailing spaces. However, your reversed
 * string should not contain leading or trailing spaces.
 * You need to reduce multiple spaces between two words to a single space in
 * the reversed string.
 * 
 * 
 * Follow up: For C programmers, try to solve it in-place in O(1) space.
 * 
 */
class Solution {
public:
    void reverseWords(string &s) {
        // first trim
        int i=0;
        int j=0;
        while (i<s.size() && j<s.size()) {
            while (j < s.size() && s[j] == ' ' && (!j || s[j-1] == ' ')) {
                j++;
            }
            if (j < s.size())
                s[i++] = s[j++];
        }
        if (i && s[i-1] == ' ')
            i--;
        s.resize(i);

        // then reverse
        reverse(s.begin(), s.end());
        if (!s.size())
            return;

        // reverse one more time
        int start = -1;
        for (int i=0; i<s.size(); ++i) {
            if (s[i] != ' ')  {
                if (!i || s[i-1] == ' ') {
                    start = i;
                }
            } else {
                if (i && s[i-1] != ' ') {
                    //cout<<start<<" "<<i<<endl; cout<<s.substr(start, i)<<endl;
                    reverse(s.begin() + start, s.begin() + i);
                }
            }
        }
        reverse(s.begin() + start, s.end());
    }

    void test() {
        string s("  the sky is blue  ");
        reverseWords(s);
        cout<<s<<endl;
    }
};
