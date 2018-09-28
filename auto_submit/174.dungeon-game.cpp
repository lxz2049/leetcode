/*
 * [174] Dungeon Game
 *
 * https://leetcode.com/problems/dungeon-game/description/
 *
 * algorithms
 * Hard (25.08%)
 * Total Accepted:    55.3K
 * Total Submissions: 218.8K
 * Testcase Example:  '[[-2,-3,3],[-5,-10,1],[10,30,-5]]'
 *
 * table.dungeon, .dungeon th, .dungeon td {
 * ⁠ border:3px solid black;
 * }
 * 
 * ⁠.dungeon th, .dungeon td {
 * ⁠   text-align: center;
 * ⁠   height: 70px;
 * ⁠   width: 70px;
 * }
 * 
 * The demons had captured the princess (P) and imprisoned her in the
 * bottom-right corner of a dungeon. The dungeon consists of M x N rooms laid
 * out in a 2D grid. Our valiant knight (K) was initially positioned in the
 * top-left room and must fight his way through the dungeon to rescue the
 * princess.
 * 
 * The knight has an initial health point represented by a positive integer. If
 * at any point his health point drops to 0 or below, he dies immediately.
 * 
 * Some of the rooms are guarded by demons, so the knight loses health
 * (negative integers) upon entering these rooms; other rooms are either empty
 * (0's) or contain magic orbs that increase the knight's health (positive
 * integers).
 * 
 * In order to reach the princess as quickly as possible, the knight decides to
 * move only rightward or downward in each step.
 * 
 * 
 * 
 * Write a function to determine the knight's minimum initial health so that he
 * is able to rescue the princess.
 * 
 * For example, given the dungeon below, the initial health of the knight must
 * be at least 7 if he follows the optimal path RIGHT-> RIGHT -> DOWN ->
 * DOWN.
 * 
 * 
 * 
 * 
 * -2 (K)
 * -3
 * 3
 * 
 * 
 * -5
 * -10
 * 1
 * 
 * 
 * 10
 * 30
 * -5 (P)
 * 
 * 
 * 
 * 
 * 
 * 
 * Note:
 * 
 * 
 * The knight's health has no upper bound.
 * Any room can contain threats or power-ups, even the first room the knight
 * enters and the bottom-right room where the princess is imprisoned.
 * 
 * 
 */
class Solution {
private:
    vector<vector<int>> dp;
    vector<vector<bool>> visited;
public:
    int calculateMinimumHP(vector<vector<int>>& dungeon) {
        dp = dungeon;
        visited = vector<vector<bool>>(dp.size(), vector<bool>(dp[0].size()));
        int minimum = traverse(dungeon, 0, 0);
        return minimum > 0 ? 1 : (1 - minimum);
    }

    int traverse(vector<vector<int>>& dungeon, int i, int j) {
        if (visited[i][j])  return dp[i][j];

        bool down = i < dungeon.size() - 1;
        bool right = j < dungeon[0].size() - 1;
        if (down && right) {
            dp[i][j] = min(dp[i][j], dp[i][j] + max(traverse(dungeon, i+1, j), traverse(dungeon, i, j+1)));
        } else if (down) {
            dp[i][j] = min(dp[i][j], dp[i][j] + traverse(dungeon, i+1, j));
        } else if (right) {
            dp[i][j] = min(dp[i][j], dp[i][j] + traverse(dungeon, i, j+1));
        }

        visited[i][j] = true;
        return dp[i][j];
    }

    void test() {
        //vector<vector<int>> dungeon = {{-2, -3, 3}, {-5, -10, 1}, {10, 30, -5}};
        vector<vector<int>> dungeon = {{1, -3, 3}, {0, -2, 0}, {-3, -3, -3}};
        //vector<vector<int>> dungeon = {{0, 0, 0}, {1, 1, -1}};
        cout<<calculateMinimumHP(dungeon)<<endl;
        for (int i=0; i<dp.size(); ++i) {
            for (int j=0; j<dp[0].size(); ++j) {
                cout<<dp[i][j]<<" ";
            }
            cout<<endl;
        }
    }
};
