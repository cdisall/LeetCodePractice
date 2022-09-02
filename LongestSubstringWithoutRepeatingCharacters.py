class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        ptr1 = 0
        ptr2 = 0
        longest = 1
        d = {}
        while ptr2 < len(s):
            if s[ptr2] in d:
                ptr1 = max(ptr1, d[s[ptr2]] + 1)
            longest = max(longest, ptr2 - ptr1 + 1)
            d[s[ptr2]] = ptr2
            ptr2 += 1
        return longest