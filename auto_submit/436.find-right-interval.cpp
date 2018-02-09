/*
 * [436] Find Right Interval
 *
 * https://leetcode.com/problems/find-right-interval/description/
 *
 * algorithms
 * Medium (41.52%)
 * Total Accepted:    16.8K
 * Total Submissions: 40.4K
 * Testcase Example:  '[[1,2]]'
 *
 * 
 * Given a set of intervals, for each of the interval i, check if there exists
 * an interval j whose start point is bigger than or equal to the end point of
 * the interval i, which can be called that j is on the "right" of i.
 * 
 * 
 * 
 * For any interval i, you need to store the minimum interval j's index, which
 * means that the interval j has the minimum start point to build the "right"
 * relationship for interval i. If the interval j doesn't exist, store -1 for
 * the interval i. Finally, you need output the stored value of each interval
 * as an array.
 * 
 * 
 * Note:
 * 
 * You may assume the interval's end point is always bigger than its start
 * point.
 * You may assume none of these intervals have the same start point.
 * 
 * 
 * 
 * Example 1:
 * 
 * Input: [ [1,2] ]
 * 
 * Output: [-1]
 * 
 * Explanation: There is only one interval in the collection, so it outputs
 * -1.
 * 
 * 
 * 
 * Example 2:
 * 
 * Input: [ [3,4], [2,3], [1,2] ]
 * 
 * Output: [-1, 0, 1]
 * 
 * Explanation: There is no satisfied "right" interval for [3,4].
 * For [2,3], the interval [3,4] has minimum-"right" start point;
 * For [1,2], the interval [2,3] has minimum-"right" start point.
 * 
 * 
 * 
 * Example 3:
 * 
 * Input: [ [1,4], [2,3], [3,4] ]
 * 
 * Output: [-1, 2, -1]
 * 
 * Explanation: There is no satisfied "right" interval for [1,4] and [3,4].
 * For [2,3], the interval [3,4] has minimum-"right" start point.
 * 
 * 
 */
/**
 * Definition for an interval.
 * struct Interval {
 *     int start;
 *     int end;
 *     Interval() : start(0), end(0) {}
 *     Interval(int s, int e) : start(s), end(e) {}
 * };
 */
struct Interval_I {
    Interval I;
    int i;
    Interval_I(Interval I, int i): I(Interval(I.start, I.end)), i(i) {}
    bool operator<(const Interval_I& _I) const {
        return I.start < _I.I.start;
    }
};

class Solution {
public:
    vector<int> findRightInterval(vector<Interval>& intervals) {
        int size = intervals.size();
        vector<Interval_I> intervalIs;
        for (int i=0; i<size; ++i) {
            intervalIs.push_back(Interval_I(intervals[i], i));   
        }
        sort(intervalIs.begin(), intervalIs.end());
 
        /*
        for (int i=0; i<intervals.size(); ++i)
            cout<<intervals[i].start<<' '<<intervals[i].end<<' ';
        cout<<endl;
        */
        
        vector<int> ans(size);
 
        for (int i=0; i<size; ++i) {
            int ii = intervalIs[i].i;
            int target = intervalIs[i].I.end;
            int l = 0, r = size - 1;
            int mid;
            while (l<=r) {
                //printf("l:%d r:%d\n", l, r);
                mid = (l+r)/2;
                if (intervalIs[mid].I.start == target)
                    break;
                else if (intervalIs[mid].I.start > target)
                    r = mid - 1;
                else
                    l = mid + 1;
            }
            if (intervalIs[mid].I.start == target)
                ans[ii] = intervalIs[mid].i;
            else if (l < size)
                ans[ii] = intervalIs[l].i;
            else
                ans[ii] = -1;
            //printf("target:%d mid:%d intervals[mid].start:%d ans[i]:%d\n", target, mid, intervals[mid].start, ans[i]);
        }
 
        return ans;
    }

    static bool cmp(const Interval &a, const Interval &b) {
        return a.start < b.start;
    }

    bool test() {
        Interval a1[] = {Interval(1, 4), Interval(2, 3), Interval(3, 4)};
        vector<Interval> v1(a1, a1+3);
        vector<int> ans = findRightInterval(v1);
        bool f1 = ans[0] == -1 && ans[1] == 2 && ans[2] == -1;

        Interval a2[] = {Interval(3, 4), Interval(2, 3), Interval(0, 1)};
        vector<Interval> v2(a2, a2+3);
        vector<int> ans2 = findRightInterval(v2);
        bool f2 = ans2[0] == -1 && ans2[1] == 0 && ans2[2] == 1;

        return f1 && f2;
    }
};
