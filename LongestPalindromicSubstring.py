class Solution(object):
    def longestPalindrome(self, s):
        if not s:
            return ""
        else:
            a = 0
            b = 0
            for i in range(0, len(s)):
                max_len = max(self.get_length(s, i, i), self.get_length(s, i, i + 1))
                if max_len > b - a:
                    a = i - (max_len - 1) / 2
                    b = i + max_len / 2
            return s[int(a):int(b)+1]

    # Find max palindrome around i
    def get_length(self, s, a, b):
        while a > -1 and b < len(s) and s[a] == s[b]:
            a -= 1
            b += 1
        return b - a - 1


#Test
if __name__ == "__main__":
    obj = Solution()
    print(Solution.longestPalindrome(obj, "abbaa"))



