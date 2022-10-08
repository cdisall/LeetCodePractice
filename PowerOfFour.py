class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n > 0:
            return not (n & (n-1)) and n & 1431655765 == n
        return False

