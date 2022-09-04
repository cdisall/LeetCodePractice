class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        m = [0] * n
        
        def minCost(cost, n):
            if n < 0:   
                return 0 
            if n == 0 or n == 1:
                return cost[n]
            if (m[n] != 0):
                return m[n]
            m[n] = cost[n] + min(minCost(cost, n-1), minCost(cost, n-2))
            return m[n]
        
        return min(minCost(cost, n-1), minCost(cost, n-2))