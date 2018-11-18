
class Solution {
public:
    ListNode *reverseKGroup(ListNode *head, int k) {
        ListNode *iter = head;
        ListNode *prev = NULL;
        while (iter) {
            //printf("%d\n", iter->val);
            ListNode *iHead = iter;
            ListNode *iPrev = NULL;

            // reverse k group
            int cnt = k;
            while (cnt-- && iter) {
                ListNode *next = iter->next;
                iter->next = iPrev;
                //printf("iter:%d next:%d prev:%d\n", iter->val, next ? next->val : -1, iPrev ? iPrev->val: -1);

                iPrev = iter;
                iter = next;
            }
            // connect reversed group to prev
            if (prev)
                prev->next = iPrev;
            else
                head = iPrev;
            // connect reversed group to next
            iHead->next = iter;

            // unreverse k-cnt group
            if (cnt >= 0) {
                k -= cnt + 1;
                iter = iPrev;
            } else {
                // update prev
                prev = iHead;
            }
        }
        return head;
    }
};

