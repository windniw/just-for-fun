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
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        if (lists.empty()) return NULL;
        vector<ListNode*> t = merge(lists);
        while (t.size() > 1){
            t = merge(t);
        }
        return t[0];
    }
    
    vector<ListNode*> merge(vector<ListNode*> &lists){
        vector<ListNode*> t;
        int len = lists.size();
        for (int i=0;i<len/2;i++)
            t.push_back(mergeTwoLists(lists[i], lists[len-i-1]));
        if (len & 0x1) t.push_back(lists[len/2]);
        return t;
    }
   
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        ListNode *l = new ListNode(0), *t = l;
        while (l1 && l2){
            if (l1->val <= l2->val){
                t->next = l1;
                l1 = l1->next;
            } else {
                t->next = l2;
                l2 = l2->next;
            }
            t = t -> next;
        }
        if (l1) t->next = l1;
        else t->next = l2;
        return l->next;
    }
};
