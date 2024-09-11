# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return None
        res = ListNode(head.val)
        curr_res = res
        while (head.next):
            if not curr_res.val == head.val:
                curr_res.next = ListNode(head.val)
                curr_res = curr_res.next
            head = head.next

        if not curr_res.val == head.val:
            curr_res.next = ListNode(head.val)
            curr_res = curr_res.next
            head = head.next

        return res
        