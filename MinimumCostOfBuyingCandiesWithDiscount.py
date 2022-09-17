class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse=True)
        res = i = 0
        n = len(cost)
        for i in range(n):
            res += sum(cost[i:i+2])
            i += 3
        return res