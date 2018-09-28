/*
 * [357] Count Numbers with Unique Digits
 *
 * https://leetcode.com/problems/count-numbers-with-unique-digits/description/
 *
 * algorithms
 * Medium (46.16%)
 * Total Accepted:    53.1K
 * Total Submissions: 115.1K
 * Testcase Example:  '2'
 *
 * Given a non-negative integer n, count all numbers with unique digits, x,
 * where 0 ≤ x < 10n.
 * 
 * 
 * Example:
 * 
 * 
 * Input: 2
 * Output: 91 
 * Explanation: The answer should be the total numbers in the range of 0 ≤ x <
 * 100, 
 * excluding 11,22,33,44,55,66,77,88,99
 * 
 * 
 * 
 */
class Solution {
public:
    int countNumbersWithUniqueDigits(int n) {
        int ret = 1;       
        for (int i = 1; i <= min(n, 10); ++i) {
            int sum = 9;
            for (int j = 1; j < i; ++j) {
                sum *= 10 - j;
            }
            ret += sum;
        }
        return ret;
    }
};
