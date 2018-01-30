/*
 * [275] H-Index II
 *
 * https://leetcode.com/problems/h-index-ii/description/
 *
 * algorithms
 * Medium (34.79%)
 * Total Accepted:    58.7K
 * Total Submissions: 168.8K
 * Testcase Example:  '[]'
 *
 * 
 * Follow up for H-Index: What if the citations array is sorted in ascending
 * order? Could you optimize your algorithm?
 * 
 */
class Solution {
public:
    int hIndex(vector<int>& citations) {	       
		// binary search
		int size = citations.size();
		int l = 0, r = size-1;
		int mid, h;
		bool found=false;
		while (l<=r && !found) {
			mid = (l+r) / 2;
			h = size-mid;
			//printf("l:%d r:%d mid:%d h:%d citations[mid]:%d\n", l, r, mid, h, citations[mid]);
			if (citations[mid] == h)
				found = true;
			else if (citations[mid] > h)
				// h can be bigger, keep searching to the left
				r = mid-1;
			else
				// h is too high, not enough citations, go to the right
				l = mid+1;
		}

		//printf("l:%d r:%d mid:%d h:%d citations[mid]:%d\n", l, r, mid, h, citations[mid]);
		if (found)
			return h;
		return size-r-1;
    }

	bool test() {
		int a[] = {3, 0, 6, 1, 5};
		sort(a, a+5);
		vector<int> va(a, a+5);
		int b[] = {1, 5, 5, 5, 5};
		vector<int> vb(b, b+5);
		return hIndex(va) == 3 && hIndex(vb) == 4;
	}
};
