/*
 * [42] Trapping Rain Water
 *
 * https://leetcode.com/problems/trapping-rain-water/description/
 *
 * algorithms
 * Hard (37.43%)
 * Total Accepted:    148K
 * Total Submissions: 395.5K
 * Testcase Example:  '[]'
 *
 * 
 * Given n non-negative integers representing an elevation map where the width
 * of each bar is 1, compute how much water it is able to trap after
 * raining. 
 * 
 * 
 * 
 * For example, 
 * Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.
 * 
 * 
 * 
 * 
 * The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1].
 * In this case, 6 units of rain water (blue section) are being trapped. Thanks
 * Marcos for contributing this image!
 */
class Solution {
public:
    int trap(vector<int>& height) {
		int lmax = 0, rmax = 0;
		int i = 0, j = height.size()-1;
		int ans = 0;

		while (i <= j) {
			// update lmax and rmax
			lmax = max(lmax, height[i]);
			rmax = max(rmax, height[j]);

			// for position i, lmax is fixed while rmax can still be higher
			// so if lmax < rmax we can safely conclude max=lmax
			if (lmax < rmax) {
				ans += lmax - height[i++];
				//printf("l<r:%d\n", ans);
			}
			// vice-versa for position j
			else {
				ans += rmax - height[j--];
				//printf("l>r:%d\n", ans);
			}
		}

		return ans;
	}
};

