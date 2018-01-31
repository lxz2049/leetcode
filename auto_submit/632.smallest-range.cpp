/*
 * [632] Smallest Range
 *
 * https://leetcode.com/problems/smallest-range/description/
 *
 * algorithms
 * Hard (42.32%)
 * Total Accepted:    7.5K
 * Total Submissions: 17.7K
 * Testcase Example:  '[[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]'
 *
 * You have k lists of sorted integers in ascending order. Find the smallest
 * range that includes at least one number from each of the k lists. 
 * 
 * We define the range [a,b] is smaller than range [c,d] if b-a < d-c or a < c
 * if b-a == d-c.
 * 
 * Example 1:
 * 
 * Input:[[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]
 * Output: [20,24]
 * Explanation: 
 * List 1: [4, 10, 15, 24,26], 24 is in range [20,24].
 * List 2: [0, 9, 12, 20], 20 is in range [20,24].
 * List 3: [5, 18, 22, 30], 22 is in range [20,24].
 * 
 * 
 * 
 * 
 * Note:
 * 
 * The given list may contain duplicates, so ascending order means >= here.
 * 1 k 
 * ⁠-105 value of elements 5.
 * For Java users, please note that the input type has been changed to
 * List<List<Integer>>. And after you reset the code template, you'll see this
 * point.
 * 
 * 
 * 
 */
class Solution {
public:
    vector<int> smallestRange(vector<vector<int> >& nums) {
		int n=0;
		int k=nums.size();
		for (int i=0; i<k; ++i) {
			n += nums[i].size();
		}
		//printf("n: %d\n", n);
		// merge all k lists
		vector<int> ids(k);
		vector<int> merged_nums(n);
		vector<int> merged_nums_j(n);
		for (int i=0; i<n; ++i) {
			int min = 0x7fffffff;
			int min_j;
			for (int j=0; j<k; ++j) {
				if (ids[j] < nums[j].size() 
						&& nums[j][ids[j]] < min) {
					min = nums[j][ids[j]];
					min_j = j;
				}
			}
			merged_nums[i] = min;
			merged_nums_j[i] = min_j;
			ids[min_j]++;
		}
		/*
		for (int i=0; i<n; ++i)
			printf("%2d ", merged_nums[i]);
		printf("\n");
		for (int i=0; i<n; ++i)
			printf("%2d ", merged_nums_j[i]);
		printf("\n\n");
		*/
		// sliding window
		int winstart_i = 0, winend_i = k;
		int winstart_min = 0, winend_min = n, winsize_min = 0x7ffffff;
		int winprogress = 0;
		vector<int> winflag(k);
		for (int i=0; i<n; ++i) {
			int num = merged_nums[i];
			int j = merged_nums_j[i];
			//printf("i:%d num:%d j:%d\n", i, num, j);
			// update winprogress
			if (winprogress < k && !winflag[j]) {
				winprogress++;
				//printf("mark winflag at %d with progress %d\n", j, winprogress);
			}
			// update winflag
			winflag[j]++;
			// move winstart_i forward and update winsize
			while (winflag[merged_nums_j[winstart_i]] > 1) {
				winflag[merged_nums_j[winstart_i++]]--;
				//printf("new winstart_i:%d\n", winstart_i);
			}
			int winstart = merged_nums[winstart_i];
			int winend = merged_nums[i];
			int winsize = winend - winstart;
			//printf("new window:%d-%d\n", winstart, winend);

			// record mins
			if (winprogress >= k && winsize < winsize_min) {
				//printf("record smaller window\n");
				winstart_min = winstart;
				winend_min = winend;
				winsize_min = winsize;
			}
			//printf("\n");
		}
		
		vector<int> ans;
		ans.push_back(winstart_min);
		ans.push_back(winstart_min+winsize_min);
		//printf("ans %d %d\n", winstart_min, winsize_min);
		return ans;
    }

	bool test() {
		int a[] = {4,10,15,24,26};
		int b[] = {0,9,12,20};
		int c[] = {5,18,22,30};
		vector<vector<int> > v1;
		v1.push_back(vector<int>(a, a+5));
		v1.push_back(vector<int>(b, b+4));
		v1.push_back(vector<int>(c, c+4));
		vector<int> ans1 = smallestRange(v1);

		int d[] = {47,67,82,97};
		int e[] = {-2,34,42,49,50,50,51};
		int f[] = {-61,-45,-3,-1,2,10};
		int g[] = {25,57,76,77,78};
		int h[] = {-11,10,29,55,55,55,57,59,60,60,62,63};
		vector<vector<int> > v2;
		v2.push_back(vector<int>(d, d+4));
		v2.push_back(vector<int>(e, e+7));
		v2.push_back(vector<int>(f, f+6));
		v2.push_back(vector<int>(g, g+5));
		v2.push_back(vector<int>(h, h+12));
		vector<int> ans2 = smallestRange(v2);

		return ans1[0] == 20 && ans1[1] == 24 && ans2[0] == 10 && ans2[1] == 47;
	}
};
