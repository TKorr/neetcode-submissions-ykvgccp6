# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head

        l,r = dummy, head

        cnt = 0
        while r:
            r = r.next
            if cnt >= n:
                l = l.next
            cnt += 1

        l.next = l.next.next
        
        return dummy.next