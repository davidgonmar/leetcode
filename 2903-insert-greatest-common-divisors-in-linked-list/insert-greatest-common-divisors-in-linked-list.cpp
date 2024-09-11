/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    int gcd(int a, int b) {
        if(b == 0) {
                return a;
        }
        else {
            return gcd(b, a % b);
        }
    }
    ListNode* insertGreatestCommonDivisors(ListNode* head) {
        ListNode *current = head;
        while (current->next) {
            ListNode *a = current;
            ListNode *b = current->next;
            int _gcd = this->gcd(a->val, b->val);
            ListNode *ln_gcd = new ListNode(_gcd, b);
            a->next = ln_gcd;
            current = ln_gcd->next;
        }
        return head;
    }
};