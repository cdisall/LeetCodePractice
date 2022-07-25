class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        p = abs(dividend)
        q = abs(divisor)
        res = 0
        # While dividend >= divisor
        while p >= q:
            a = 0
            # Find the highest power of 2 in the dividend
            while p > (q << (a+1)):
                a += 1
            # Add highest power to answer
            res += (1<<a)
            # Update dividend
            p -= (q<<a)
        if (dividend < 0) is not (divisor < 0):
            return -res
        return min(max(-2147483648, res), 2147483647)