# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapNodes(self, head, k):
        ptr = ptr1 = ptr2 = head
        i = 1
        while ptr:
            if i < k:
                ptr1 = ptr1.next
            if i > k:
                ptr2 = ptr2.next
            ptr = ptr.next
            i += 1
        ptr1.val, ptr2.val = ptr2.val, ptr1.val

        return head



