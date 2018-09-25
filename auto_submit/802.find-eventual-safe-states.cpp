/*
 * [820] Find Eventual Safe States
 *
 * https://leetcode.com/problems/find-eventual-safe-states/description/
 *
 * algorithms
 * Medium (40.44%)
 * Total Accepted:    8.9K
 * Total Submissions: 21.9K
 * Testcase Example:  '[[1,2],[2,3],[5],[0],[5],[],[]]'
 *
 * In a directed graph, we start at some node and every turn, walk along a
 * directed edge of the graph.  If we reach a node that is terminal (that is,
 * it has no outgoing directed edges), we stop.
 * 
 * Now, say our starting node is eventually safe if and only if we must
 * eventually walk to a terminal node.  More specifically, there exists a
 * natural number K so that for any choice of where to walk, we must have
 * stopped at a terminal node in less than K steps.
 * 
 * Which nodes are eventually safe?  Return them as an array in sorted order.
 * 
 * The directed graph has N nodes with labels 0, 1, ..., N-1, where N is the
 * length of graph.  The graph is given in the following form: graph[i] is a
 * list of labels j such that (i, j) is a directed edge of the graph.
 * 
 * 
 * Example:
 * Input: graph = [[1,2],[2,3],[5],[0],[5],[],[]]
 * Output: [2,4,5,6]
 * Here is a diagram of the above graph.
 * 
 * 
 * 
 * 
 * 
 * Note:
 * 
 * 
 * graph will have length at most 10000.
 * The number of edges in the graph will not exceed 32000.
 * Each graph[i] will be a sorted list of different integers, chosen within the
 * range [0, graph.length - 1].
 * 
 */
class Solution {
private:
    vector<int> visited;
public:
    bool traverse(vector<vector<int>>& graph, int n) {
        visited[n] = 1;
        bool valid = true;
        for (int i=0; i<graph[n].size(); ++i) {
            int next = graph[n][i];
            if (!visited[next]) {
                valid &= traverse(graph, next);
            } else if (visited[next] == 1) {
                valid = false;
            }
        }
        visited[n] = valid ? 2 : 1;
        //cout<<n<<" "<<visited[n]<<endl;
        return valid;
    }

    vector<int> eventualSafeNodes(vector<vector<int>>& graph) {
        visited.assign(graph.size(), 0);
        for (int i=0; i<graph.size(); ++i)
            if (!visited[i])
                traverse(graph, i);
        vector<int> ret;
        for (int i=0; i<visited.size(); ++i) {
            if (visited[i] != 1) {
                ret.push_back(i);
            }
        }
        return ret;
    }

    void test() {
        vector<vector<int>> graph {{0}, {2,3,4}, {3,4}, {0,4}, {}};
        eventualSafeNodes(graph);
    }
};
