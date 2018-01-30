/*
 * [274] H-Index
 *
 * https://leetcode.com/problems/h-index/description/
 *
 * algorithms
 * Medium (33.67%)
 * Total Accepted:    91K
 * Total Submissions: 270.1K
 * Testcase Example:  '[]'
 *
 * 
 * Given an array of citations (each citation is a non-negative integer) of a
 * researcher, write a function to compute the researcher's h-index.
 * 
 * 
 * 
 * According to the definition of h-index on Wikipedia: "A scientist has index
 * h if h of his/her N papers have at least h citations each, and the other N −
 * h papers have no more than h citations each."
 * 
 * 
 * 
 * For example, given citations = [3, 0, 6, 1, 5], which means the researcher
 * has 5 papers in total and each of them had received 3, 0, 6, 1, 5 citations
 * respectively. Since the researcher has 3 papers with at least 3 citations
 * each and the remaining two with no more than 3 citations each, his h-index
 * is 3.
 * 
 * 
 * 
 * Note: If there are several possible values for h, the maximum one is taken
 * as the h-index.
 * 
 * 
 * Credits:Special thanks to @jianchao.li.fighter for adding this problem and
 * creating all test cases.
 */
class Solution {
public:
    int hIndex(vector<int>& c) {
		int i;
		int size=c.size();
		vector<int> v(size+1);
 		for (i=1; i<=size; ++i) {
			v[c[i-1] > size ? size : c[i-1]]++;
		}       
		int n=0;
		int h=0;
		for (i=size; i>=1; --i) {
			n += v[i];
			h = max(h, min(n, i));
		}

		return h;
    }

	bool test() {
		int a[] = {3, 0, 6, 1, 5};
		vector<int> v(a, a+5);
		return hIndex(v) == 3;
	}
};
