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
		// create a copy of height
		int size = height.size();
		vector<int>water(height);

		// store lmax
		int lmax=0;
		for (int i=0; i<size-1; ++i) {
			if (height[i] > lmax)
				lmax = height[i];
			water[i] = lmax;
		}

		// store rmax
		int rmax = 0;
		for (int i=size-1; i>0; --i) {
			if (height[i] > rmax)
				rmax = height[i];
			water[i] = min(rmax, water[i]);
		}

		// get result
		int ans=0;
		for (int i=0; i<size; ++i) {
			//printf("%d ", water[i]);
			ans += water[i] - height[i];
		}
		//printf("\n");

		return ans;
    }
};

