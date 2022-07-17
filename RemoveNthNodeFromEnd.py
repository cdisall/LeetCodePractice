# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head, n: int):
        ptr1=head
        ptr2=head
        # Offset start of pointer 1 by n
        for i in range(n):
            ptr1 = ptr1.next
        # Check that pointer 1 is not the last node
        if not ptr1:
            return head.next
        # Iterate through nodes until pointer 1 reaches end
        while ptr1.next:
            ptr2 = ptr2.next
            ptr1 = ptr1.next
        ptr2.next = ptr2.next.next
        return head


