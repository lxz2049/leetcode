/*
 * [744] Network Delay Time
 *
 * https://leetcode.com/problems/network-delay-time/description/
 *
 * algorithms
 * Medium (37.03%)
 * Total Accepted:    11.5K
 * Total Submissions: 31.1K
 * Testcase Example:  '[[2,1,1],[2,3,1],[3,4,1]]\n4\n2'
 *
 * 
 * There are N network nodes, labelled 1 to N.
 * 
 * Given times, a list of travel times as directed edges times[i] = (u, v, w),
 * where u is the source node, v is the target node, and w is the time it takes
 * for a signal to travel from source to target.
 * 
 * Now, we send a signal from a certain node K.  How long will it take for all
 * nodes to receive the signal?  If it is impossible, return -1.
 * 
 * 
 * Note:
 * 
 * N will be in the range [1, 100].
 * K will be in the range [1, N].
 * The length of times will be in the range [1, 6000].
 * All edges times[i] = (u, v, w) will have 1  and 1 .
 * 
 * 
 */
const int MAX_DIST = 10001;
class Solution {
public:
    int networkDelayTime(vector<vector<int>>& times, int N, int K) {
        int graph[N+1][N+1];
        for (int i=0; i<N+1; ++i) 
            for (int j=0; j<N+1; ++j)
                graph[i][j] = MAX_DIST;
        for (int i=0; i<times.size(); ++i) {
            int u = times[i][0];
            int v = times[i][1];
            graph[u][v] = times[i][2];
        }

        bool visited[N+1]; fill_n(visited, N+1, 0);
        int dist[N+1]; fill_n(dist, N+1, MAX_DIST);
        dist[K] = 0;
        while (true) {
            int minDist = MAX_DIST;
            int minI = -1;
            for (int i=1; i<N+1; ++i) {
                if (!visited[i] && dist[i] < minDist) {
                    minI = i;
                    minDist = dist[i];
                }
            }

            if (minI < 0)   break;

            for (int i=1; i<N+1; ++i) {
                if (graph[minI][i] >= 0) {
                    dist[i] = min(dist[i], dist[minI] + graph[minI][i]);
                }
            }
            visited[minI] = true;
        }

        int ans = 0;
        for (int i=1; i<N+1; ++i) {
            ans = max(ans, dist[i]);
        }
        return ans < MAX_DIST ? ans : -1;
    }

    void test() {
        vector<vector<int>> times = {{2,1,1}, {2,3,1}, {3,4,1}};
        cout<<networkDelayTime(times, 4, 2)<<endl;
        //vector<vector<int>> times = {{1,2,1}};
        //cout<<networkDelayTime(times, 2, 1)<<endl;
    }
};
