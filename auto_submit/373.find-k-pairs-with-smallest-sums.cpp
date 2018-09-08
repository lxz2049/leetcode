/*
 * [373] Find K Pairs with Smallest Sums
 *
 * https://leetcode.com/problems/find-k-pairs-with-smallest-sums/description/
 *
 * algorithms
 * Medium (31.79%)
 * Total Accepted:    47.5K
 * Total Submissions: 149.3K
 * Testcase Example:  '[1,7,11]\n[2,4,6]\n3'
 *
 * You are given two integer arrays nums1 and nums2 sorted in ascending order
 * and an integer k.
 * 
 * Define a pair (u,v) which consists of one element from the first array and
 * one element from the second array.
 * 
 * Find the k pairs (u1,v1),(u2,v2) ...(uk,vk) with the smallest sums.
 * 
 * Example 1:
 * 
 * 
 * Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
 * Output: [[1,2],[1,4],[1,6]] 
 * Explanation: The first 3 pairs are returned from the sequence: 
 * [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
 * 
 * Example 2:
 * 
 * 
 * Input: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
 * Output: [1,1],[1,1]
 * Explanation: The first 2 pairs are returned from the sequence: 
 * [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]
 * 
 * Example 3:
 * 
 * 
 * Input: nums1 = [1,2], nums2 = [3], k = 3
 * Output: [1,3],[2,3]
 * Explanation: All possible pairs are returned from the sequence: [1,3],[2,3]
 * 
 * 
 */
typedef tuple<int,int,int> triplet;
class Compare{
public:
  bool operator()(const triplet& a, const triplet& b) const{
      return get<2>(a) > get<2>(b);
  }
};

class Solution {
public:
    vector<pair<int, int>> kSmallestPairs(vector<int>& nums1, vector<int>& nums2, int k) {
        if (!nums1.size() || !nums2.size()) 
            return vector<pair<int, int>>();
        vector<pair<int, int>> ret;
        priority_queue<triplet, vector<triplet>, Compare> p;
        p.push(triplet(0, 0, nums1[0] + nums2[0]));
        vector<vector<bool>> visited(nums1.size(), vector<bool>(nums2.size(), 0));
        visited[0][0] = true;
        while (k-- && !p.empty()) {
            triplet t = p.top();
            p.pop();
            int i = get<0>(t);
            int j = get<1>(t);
            ret.push_back({nums1[i], nums2[j]});
            if (i + 1 < nums1.size() && !visited[i+1][j]) {
                p.push(triplet(i+1, j, nums1[i+1] + nums2[j]));
                visited[i+1][j] = true;
            }
            if (j + 1 < nums2.size() && !visited[i][j+1]) {
                p.push(triplet(i, j+1, nums1[i] + nums2[j+1]));
                visited[i][j+1] = true;
            }
        }
        return ret;
    }

    void test() {
        vector<int> v1 = {-10,-4,0,0,6};
        vector<int> v2 = {3,5,6,7,8,100};
        vector<pair<int ,int>> ret = kSmallestPairs(v1, v2, 10);
        for (int i=0; i<ret.size(); ++i) {
            cout<<ret[i].first<<" "<<ret[i].second<<endl;
        }
    }
};
