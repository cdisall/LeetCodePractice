class Solution(object):
    def reverse(self, x):
        sign = 1
        min = -2 ** 31
        max = 2 ** 31-1
        ans = 0
        if x<0:
            sign = -1
            x = -x
        while(x > 0):
            ans = ans * 10
            ans += x % 10
            x //= 10
        if ans >= max or ans <= min:
            return 0
        if sign == -1:
            return -ans
        else:
            return ans


#Test
if __name__ == "__main__":
    obj = Solution()
    print(Solution.reverse(obj, -123))