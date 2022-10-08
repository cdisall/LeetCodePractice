class Solution:
    def longestCommonPrefix(self, strs):
        s = strs[0]
        for i in strs:
            while not i.startswith(s):
                s = s[:-1]
        return s
      
