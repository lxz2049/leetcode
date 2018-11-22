/*
 * [715] Range Module
 *
 * https://leetcode.com/problems/range-module/description/
 *
 * algorithms
 * Hard (31.34%)
 * Total Accepted:    7.2K
 * Total Submissions: 22.2K
 * Testcase Example:  '["RangeModule","addRange","removeRange","queryRange","queryRange","queryRange"]\n[[],[10,20],[14,16],[10,14],[13,15],[16,17]]'
 *
 * A Range Module is a module that tracks ranges of numbers. Your task is to
 * design and implement the following interfaces in an efficient manner.
 * 
 * addRange(int left, int right) Adds the half-open interval [left, right),
 * tracking every real number in that interval.  Adding an interval that
 * partially overlaps with currently tracked numbers should add any numbers in
 * the interval [left, right) that are not already tracked.
 * 
 * queryRange(int left, int right) Returns true if and only if every real
 * number in the interval [left, right)
 * ⁠is currently being tracked.
 * 
 * removeRange(int left, int right) Stops tracking every real number currently
 * being tracked in the interval [left, right).
 * 
 * Example 1:
 * 
 * addRange(10, 20): null
 * removeRange(14, 16): null
 * queryRange(10, 14): true (Every number in [10, 14) is being tracked)
 * queryRange(13, 15): false (Numbers like 14, 14.03, 14.17 in [13, 15) are not
 * being tracked)
 * queryRange(16, 17): true (The number 16 in [16, 17) is still being tracked,
 * despite the remove operation)
 * 
 * 
 * 
 * Note:
 * A half open interval [left, right) denotes all real numbers left .
 * 
 * 0 < left < right < 10^9 in all calls to addRange, queryRange, removeRange.
 * The total number of calls to addRange in a single test case is at most 1000.
 * The total number of calls to queryRange in a single test case is at most
 * 5000.
 * The total number of calls to removeRange in a single test case is at most
 * 1000.
 * 
 */
typedef set<pair<int, int>> Range;
class RangeModule {
private:
    Range ranges;
public:
    RangeModule() {
        ranges.clear();
    }
    
    void addRange(int start, int end) {
        Range::iterator left = ranges.end();
        Range::iterator right = ranges.end();
        for (Range::iterator it = ranges.begin(); it != ranges.end(); ++it) {
            int l = it->first;
            int r = it->second;
            if (start <= r && left == ranges.end()) {
                start = min(start, l);
                left = it;
            }
            if (end < l && right == ranges.end()) {
                right = it;
            }
            if (end >= l) {
                end = max(end, r);
            }
        }
        ranges.erase(left, right);
        ranges.insert({start, end});
    }
    
    bool queryRange(int start, int end) {
        pair<int, int> target(start, 0x7fffffff);
        Range::iterator it = ranges.lower_bound(target);
        if (it != ranges.begin()) {
            it = prev(it);
        }
        int l = it->first;
        int r = it->second;
        return l <= start && end <= r;
    }
    
    void removeRange(int start, int end) {
        Range::iterator left = ranges.end();
        Range::iterator right = ranges.end();
        int lo = start;
        int hi = end;
        for (Range::iterator it = ranges.begin(); it != ranges.end(); ++it) {
            int l = it->first;
            int r = it->second;
            if (start <= r && left == ranges.end()) {
                lo = l;
                left = it;
            }
            if (end < l && right == ranges.end()) {
                right = it;
            }
            if (end >= l) {
                hi = r;
            }
        }
        ranges.erase(left, right);
        if (lo < start) ranges.insert({lo, start});
        if (end < hi) ranges.insert({end, hi});
    }

    void test() {
        for (Range::iterator it = ranges.begin(); it != ranges.end(); ++it) {
            cout<<it->first<<" "<<it->second<<endl;
        }
        cout<<endl;
    }
};

class Solution {
public:
    void test() {
        RangeModule module;
        module.addRange(10, 180);module.test();
        module.addRange(150, 200);module.test();
        module.addRange(250, 500);module.test();
        cout<<module.queryRange(50, 100)<<endl;
        cout<<module.queryRange(180, 300)<<endl;
        cout<<module.queryRange(600, 1000)<<endl;
        module.removeRange(50, 150);module.test();
        cout<<module.queryRange(50, 100)<<endl;
    }
};
