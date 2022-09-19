class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        if not g or not s:
            return 0
        numChildren = numCookies = 0
        g.sort()
        s.sort()
        while numCookies < len(s) and numChildren < len(g):
            if s[numCookies] >= g[numChildren]:
                numChildren += 1
            numCookies += 1
        return numChildren