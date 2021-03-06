# Definition for singly-linked list.
class ListNode:
   def __init__(self, val=0, next=None):
       self.val = val
       self.next = next

class Solution:
    def reverseList(self, head):
        if (not head) or (not head.next):
            return head
        next = head.next
        new_head = self.reverseList(next)
        next.next = head
        head.next = None
        return new_head