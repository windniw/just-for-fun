public class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode res = new ListNode(0), t = res;
        ListNode emp = new ListNode(0);
        int k = 0;
        while (true){
            int k1 = l1.val, k2 = l2.val;
            int sum = k1 + k2 + k;
            t.val = sum%10;
            t.next = new ListNode(0);
            k = sum / 10;
            if (l1.next!=null)
                l1 = l1.next;
            else 
                l1 = emp;
            if (l2.next!=null)
                l2 = l2.next;
            else 
                l2 = emp;
            if (l1.equals(l2) && k==0){
                t.next = null;
                break;
            }
            t = t.next;
        }
        return res;
    }
}

// ------------------
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        int t = 0, a = 0, b = 0;
        ListNode* head = NULL, *pre = NULL;
        while (1){
            a = l1 ? l1->val : 0;
            b = l2 ? l2->val : 0;
            ListNode *cur = new ListNode((a + b + t) % 10);
            if (head == NULL){
                head = cur;
                pre = cur;
            }
            else {
                pre -> next = cur;
                pre = cur;
            }
            t = (a + b + t) / 10;
            l1 = l1 ? l1->next : NULL;
            l2 = l2 ? l2->next : NULL;
            if (!l1 && !l2) break;
        }
        if (t != 0) pre -> next = new ListNode(t);
        return head;
    }
};
