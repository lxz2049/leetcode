class Solution {
public:
    int surfaceArea(vector<vector<int>>& grid) {
        int ans = 0;
        for (int i=0; i<grid.size(); ++i) {
            for (int j=0; j<grid[i].size(); ++j) {
                if (grid[i][j]) {
                        ans += 2;
                    int down = i > 0 ? grid[i-1][j] : 0;
                    int up = i < grid.size()-1 ? grid[i+1][j] : 0;
                    int left = j > 0 ? grid[i][j-1] : 0;
                    int right = j < grid[i].size()-1 ? grid[i][j+1] : 0;
                    ans += max(0, grid[i][j] - down);
                    ans += max(0, grid[i][j] - up);
                    ans += max(0, grid[i][j] - left);
                    ans += max(0, grid[i][j] - right);
                }
           }
        }       
        return ans;
    }

    void test() {
        vector<vector<int>> v = {{1,2},{3,4}};
        int ans = surfaceArea(v);
        cout<<ans<<endl;
    }
};
