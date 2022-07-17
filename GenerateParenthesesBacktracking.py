from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        l = []
        self.backtrack('', 0, 0, l, n)
        return l

    def backtrack(self, s, left, right, l, n):
        if len(s) == 2 * n:
            l.append(s)
        else:
            if left < n:
                self.backtrack(s + '(', left + 1, right, l, n)
            if right < left:
                self.backtrack(s + ')', left, right + 1, l, n)