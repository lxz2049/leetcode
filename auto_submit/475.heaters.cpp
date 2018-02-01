/*
 * [475] Heaters
 *
 * https://leetcode.com/problems/heaters/description/
 *
 * algorithms
 * Easy (29.65%)
 * Total Accepted:    25.8K
 * Total Submissions: 87.1K
 * Testcase Example:  '[1,2,3]\n[2]'
 *
 * Winter is coming! Your first job during the contest is to design a standard
 * heater with fixed warm radius to warm all the houses.
 * 
 * Now, you are given positions of houses and heaters on a horizontal line,
 * find out minimum radius of heaters so that all houses could be covered by
 * those heaters.
 * 
 * So, your input will be the positions of houses and heaters seperately, and
 * your expected output will be the minimum radius standard of heaters.
 * 
 * Note:
 * 
 * Numbers of houses and heaters you are given are non-negative and will not
 * exceed 25000.
 * Positions of houses and heaters you are given are non-negative and will not
 * exceed 10^9.
 * As long as a house is in the heaters' warm radius range, it can be warmed.
 * All the heaters follow your radius standard and the warm radius will the
 * same.
 * 
 * 
 * 
 * Example 1:
 * 
 * Input: [1,2,3],[2]
 * Output: 1
 * Explanation: The only heater was placed in the position 2, and if we use the
 * radius 1 standard, then all the houses can be warmed.
 * 
 * 
 * 
 * Example 2:
 * 
 * Input: [1,2,3,4],[1,4]
 * Output: 1
 * Explanation: The two heater was placed in the position 1 and 4. We need to
 * use radius 1 standard, then all the houses can be warmed.
 * 
 * 
 */
class Solution {
public:
    int findRadius(vector<int>& houses, vector<int>& heaters) {
		sort(houses.begin(), houses.end());
		sort(heaters.begin(), heaters.end());
		int max_min_dist = 0;
		for (int i=0, j=0; i<houses.size(); ++i) {
			// house[i] be in between heaters[j] and heaters[j+1]
			while (j<heaters.size()-1 && houses[i] > heaters[j+1]) {
				j++;
			}
			int dist_to_left = abs(houses[i]-heaters[j]);
			int dist_to_right = j<heaters.size()-1 ? heaters[j+1]-houses[i] : dist_to_left;
			//printf("i:%d houses[i]:%d j:%d heaters[j]:%d\n", i, houses[i], j, heaters[j]);
			//printf("dl:%d dr:%d\n", dist_to_left, dist_to_right);
			max_min_dist = max(max_min_dist, min(dist_to_left, dist_to_right));
		}
		return max_min_dist;
    }

	bool test() {
		int houses[] = {282475249,622650073,984943658,144108930,470211272,101027544,457850878,458777923};
		int heaters[] = {823564440,115438165,784484492,74243042,114807987,137522503,441282327,16531729,823378840,143542612};
		vector<int> vhouses(houses, houses+8);
		vector<int> vheaters(heaters, heaters+10);
		return findRadius(vhouses, vheaters) == 161834419;
	}
};
