class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        m = [0] * n
        for i in range(0,n):
            if i < 2:
                m[i] = cost[i]
            else:
                m[i] = cost[i] + min(m[i-1], m[i-2])
        return min(m[n-1], m[n-2])