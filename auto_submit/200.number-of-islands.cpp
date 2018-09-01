/*
 * [200] Number of Islands
 *
 * https://leetcode.com/problems/number-of-islands/description/
 *
 * algorithms
 * Medium (36.99%)
 * Total Accepted:    210.2K
 * Total Submissions: 556.4K
 * Testcase Example:  '[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]'
 *
 * Given a 2d grid map of '1's (land) and '0's (water), count the number of
 * islands. An island is surrounded by water and is formed by connecting
 * adjacent lands horizontally or vertically. You may assume all four edges of
 * the grid are all surrounded by water.
 * 
 * Example 1:
 * 
 * 
 * Input:
 * 11110
 * 11010
 * 11000
 * 00000
 * 
 * Output: 1
 * 
 * 
 * Example 2:
 * 
 * 
 * Input:
 * 11000
 * 11000
 * 00100
 * 00011
 * 
 * Output: 3
 * 
 * 
 */
class Solution {
public:
    void traverse(vector<vector<char>>& grid, int i, int j) {
        if (i >= 0 && i < grid.size() && j >= 0 && j < grid[i].size() 
                && grid[i][j] == '1') {
            grid[i][j] = '2';
            traverse(grid, i+1, j);
            traverse(grid, i, j+1);
            traverse(grid, i-1, j);
            traverse(grid, i, j-1);
        }
    }

    int numIslands(vector<vector<char>>& grid) {
        int ans = 0;
        for (int i = 0; i < grid.size(); ++i) {
            for (int j = 0; j < grid[i].size(); ++j) {
                if (grid[i][j] == '1')
                    ans++;
                    traverse(grid, i, j);
            }
        }       
        return ans;
    }

    void test() {
        char arr0[] = {'1','1','1','1','0'};
        vector<char> v0(arr0, arr0+5);
        char arr1[] = {'1','1','0','1','0'};
        vector<char> v1(arr1, arr1+5);
        char arr2[] = {'1','1','0','0','0'};
        vector<char> v2(arr2, arr2+5);
        char arr3[] = {'0','0','0','0','0'};
        vector<char> v3(arr3, arr3+5);
        vector<vector<char>> v;
        v.push_back(v0);
        v.push_back(v1);
        v.push_back(v2);
        v.push_back(v3);
        cout<<numIslands(v)<<endl;
    }
};
