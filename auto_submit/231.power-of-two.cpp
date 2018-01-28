/*
 * [231] Power of Two
 *
 * https://leetcode.com/problems/power-of-two/description/
 *
 * algorithms
 * Easy (40.56%)
 * Total Accepted:    160.5K
 * Total Submissions: 395.7K
 * Testcase Example:  '1'
 *
 * 
 * Given an integer, write a function to determine if it is a power of two.
 * 
 * 
 * Credits:Special thanks to @jianchao.li.fighter for adding this problem and
 * creating all test cases.
 */
class Solution {
public:
    bool isPowerOfTwo(int n) {
		return n > 0 && !(n & n-1);
    }

	bool test() {		
		return isPowerOfTwo(1)
			&& !isPowerOfTwo(0)
			&& isPowerOfTwo(2)
			&& isPowerOfTwo(4)
			&& isPowerOfTwo(8)
			&& isPowerOfTwo(16)
			&& !isPowerOfTwo(17)
			;
	}
};
