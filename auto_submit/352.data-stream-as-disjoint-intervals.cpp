/*
 * [352] Data Stream as Disjoint Intervals
 *
 * https://leetcode.com/problems/data-stream-as-disjoint-intervals/description/
 *
 * algorithms
 * Hard (41.83%)
 * Total Accepted:    20.5K
 * Total Submissions: 48.6K
 * Testcase Example:  '["SummaryRanges","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals"]\n[[],[1],[],[3],[],[7],[],[2],[],[6],[]]'
 *
 * Given a data stream input of non-negative integers a1, a2, ..., an, ...,
 * summarize the numbers seen so far as a list of disjoint intervals.
 * 
 * For example, suppose the integers from the data stream are 1, 3, 7, 2, 6,
 * ..., then the summary will be:
 * 
 * 
 * [1, 1]
 * [1, 1], [3, 3]
 * [1, 1], [3, 3], [7, 7]
 * [1, 3], [7, 7]
 * [1, 3], [6, 7]
 * 
 * 
 * Follow up:
 * What if there are lots of merges and the number of disjoint intervals are
 * small compared to the data stream's size?
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
class SummaryRanges {
private:
    set<int> bst;
public:
    /** Initialize your data structure here. */
    SummaryRanges() {
        bst.clear();
    }
    
    void addNum(int val) {
        bst.insert(val);
    }
    
    vector<Interval> getIntervals() {
        vector<Interval> ret;
        for (set<int>::iterator it=bst.begin(); it != bst.end(); it++) {
            int val = *it;
            if (!ret.empty() && ret.back().end + 1 == val)
                ret.back().end = val;
            else {
                ret.push_back(Interval(val, val));
            }
        }
        return ret;
    }

    void test() {
        for (auto i: getIntervals()) {
            cout<<i.start<<" "<<i.end<<endl;
        }
        cout<<endl;
    }
};

class Solution {
public:
    void test() {
        SummaryRanges ranges;
        ranges.addNum(1);ranges.test();
        ranges.addNum(3);ranges.test();
        ranges.addNum(7);ranges.test();
        ranges.addNum(2);ranges.test();
    }
};

/**
 * Your SummaryRanges object will be instantiated and called as such:
 * SummaryRanges obj = new SummaryRanges();
 * obj.addNum(val);
 * vector<Interval> param_2 = obj.getIntervals();
 */
