class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        if (index(head, n) == n - 1)
            return head->next;
        else
            return head;
    }
    
    int index(ListNode* cur, int n){
        cout<<cur->val<<endl;
        int pos = cur->next? index(cur->next, n)+1 : 0;
        if (pos == n)
            cur->next = n!=1 ? cur->next->next : NULL;
        return pos;
    }
};
