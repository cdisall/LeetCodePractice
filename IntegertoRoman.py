class Solution(object):
    def intToRoman(self, num):
        integer = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        roman = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX',
                 5: 'V', 4: 'IV', 1: 'I'}
        ans = ""
        for i in range(len(roman)):
            ans += (num // integer[i]) * roman[integer[i]]
            num %= integer[i]
        return ans


# Test
if __name__ == "__main__":
    obj = Solution()
    print(Solution.intToRoman(obj, 58))
