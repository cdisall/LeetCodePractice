# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head):
        if not head or not head.next:
            return head
        # Recursively call swapPairs on sublist with current pair removed
        tmp_head = self.swapPairs(head.next.next)

        # Swap current pair
        cur = head.next
        cur.next = head
        # Point to sublist
        head.next = tmp_head
        # Return head of new sublist
        return cur



