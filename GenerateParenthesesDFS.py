from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        l = []
        self.dfs('', n, n, l)
        return l

    def dfs(self, s, left, right, l):
        if left <= right:
            if left == 0 and right == 0:
                l.append(s)
                return
            if left:
                self.dfs(s + '(', left-1, right, l)
            if right:
                self.dfs(s + ')', left, right-1, l)






