/*
 * [661] Image Smoother
 *
 * https://leetcode.com/problems/image-smoother/description/
 *
 * algorithms
 * Easy (47.09%)
 * Total Accepted:    24.5K
 * Total Submissions: 51.8K
 * Testcase Example:  '[[1,1,1],[1,0,1],[1,1,1]]'
 *
 * Given a 2D integer matrix M representing the gray scale of an image, you
 * need to design a smoother to make the gray scale of each cell becomes the
 * average gray scale (rounding down) of all the 8 surrounding cells and
 * itself.  If a cell has less than 8 surrounding cells, then use as many as
 * you can.
 * 
 * Example 1:
 * 
 * Input:
 * [[1,1,1],
 * ⁠[1,0,1],
 * ⁠[1,1,1]]
 * Output:
 * [[0, 0, 0],
 * ⁠[0, 0, 0],
 * ⁠[0, 0, 0]]
 * Explanation:
 * For the point (0,0), (0,2), (2,0), (2,2): floor(3/4) = floor(0.75) = 0
 * For the point (0,1), (1,0), (1,2), (2,1): floor(5/6) = floor(0.83333333) = 0
 * For the point (1,1): floor(8/9) = floor(0.88888889) = 0
 * 
 * 
 * 
 * Note:
 * 
 * The value in the given matrix is in the range of [0, 255].
 * The length and width of the given matrix are in the range of [1, 150].
 * 
 * 
 */
class Solution {
public:
    vector<vector<int>> imageSmoother(vector<vector<int>>& M) {
        vector<vector<int>> ret(M);
        for (int i=0; i<ret.size(); ++i) {
            for (int j=0; j<ret[i].size(); ++j) {
                bool down = i < ret.size()-1;
                bool right = j < ret[i].size()-1;
                bool up = i > 0;
                bool left = j > 0;
                ret[i][j] = M[i][j] + 
                            (down ? M[i+1][j] : 0) + 
                            (right ? M[i][j+1] : 0) + 
                            (down & right ? M[i+1][j+1] : 0) + 
                            (down & left ? M[i+1][j-1] : 0) + 
                            (up ? M[i-1][j] : 0) + 
                            (left ? M[i][j-1] : 0) + 
                            (up & left ? M[i-1][j-1] : 0) +
                            (up & right ? M[i-1][j+1] : 0);
                int quo = 1 + down + right + up + left + (down & right) + (up & left) + (down & left) + (up & right);
                ret[i][j] = ret[i][j] / quo;
            }
        }
        return ret;
    }
};
