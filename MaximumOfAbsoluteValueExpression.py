class Solution:
    def maxAbsValExpr(self, arr1, arr2):
        res = 0
        for x in [-1,1]:
            for y in [-1,1]:
                mini = x * arr1[0] + y * arr2[0]
                for i in range(len(arr1)):
                    cur = x * arr1[i] + y * arr2[i] + i
                    res = max(res, cur - mini)
                    mini = min(mini, cur)
        return res