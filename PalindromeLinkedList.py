# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def isPalindrome(self, head):
        ptr1 = ptr2 = head
        reverse = None
        while ptr1 and ptr1.next:
            ptr1 = ptr1.next.next
            reverse, reverse.next, ptr2  = ptr2, reverse, ptr2.next
        if ptr1:
            ptr2 = ptr2.next
        while reverse and reverse.val == ptr2.val:
            reverse = reverse.next
            ptr2 = ptr2.next
        if reverse:
            return False
        return True