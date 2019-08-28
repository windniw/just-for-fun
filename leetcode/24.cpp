/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* swapPairs(ListNode* head) {
        ListNode *h = new ListNode(0), *t, *cur = h;
        h->next = head;
        while (cur->next && cur->next->next) {
            t = cur->next;
            cur->next = cur->next->next;
            t->next = cur->next->next;
            cur->next->next = t;
            cur = cur->next->next;
        }
        return h->next;
    }
};
