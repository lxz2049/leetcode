/*
 * [390] Elimination Game
 *
 * https://leetcode.com/problems/elimination-game/description/
 *
 * algorithms
 * Medium (42.86%)
 * Total Accepted:    19.1K
 * Total Submissions: 44.5K
 * Testcase Example:  '9'
 *
 * 
 * There is a list of sorted integers from 1 to n. Starting from left to right,
 * remove the first number and every other number afterward until you reach the
 * end of the list.
 * 
 * Repeat the previous step again, but this time from right to left, remove the
 * right most number and every other number from the remaining numbers.
 * 
 * We keep repeating the steps again, alternating left to right and right to
 * left, until a single number remains.
 * 
 * Find the last number that remains starting with a list of length n.
 * 
 * Example:
 * 
 * Input:
 * n = 9,
 * 1 2 3 4 5 6 7 8 9
 * 2 4 6 8
 * 2 6
 * 6
 * 
 * Output:
 * 6
 * 
 * 
 */
class Solution {
public:
    int lastRemaining(int n) {
        int i = 0;       
        int s = 1;
        int l = 1;
        int r = n;
        while (n > 1) {
            if (i % 2) {
                // right to left
                if (n % 2)    l += s;
                r -= s;
            } else {
                // left to right
                if (n % 2)    r -= s;
                l += s;
            }
            n /= 2;
            i = (i+1) % 2;
            s *= 2;
            //cout<<l<<" "<<r<<endl;
        }
        return l;
    }

    void test() {
        cout<<lastRemaining(1)<<endl;
        cout<<lastRemaining(2)<<endl;
        cout<<lastRemaining(3)<<endl;
        cout<<lastRemaining(4)<<endl;
        cout<<lastRemaining(9)<<endl;
    }
};
