class Solution:
    def isPalindrome(self, s: str) -> bool:
        ptr2 = 0
        s = ''.join(ch.lower() for ch in s if ch.isalnum())
        ptr1 = len(s)-1
        while ptr2 <= ptr1:
            if s[ptr2] is not s[ptr1]:
                return False
            ptr1 -= 1
            ptr2 += 1
        return True