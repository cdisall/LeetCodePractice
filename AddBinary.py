class Solution:
    def addBinary(self, a: str, b: str) -> str:
        la, lb = list(a), list(b)
        res = ""
        carry = 0
        while la or lb or carry:
            if la:
                carry += int(la.pop())
            if lb:
                carry += int(lb.pop())
            res += str(carry %2)
            carry //= 2

        return res[::-1] 
