class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return self.dp(m, n, 0, 0)
    
    def dp(self, m, n, i, j):
        if i == m-1 and j == n-1:
            return 1
        if i < m-1 and j < n-1:
            return self.dp(m, n, i+1, j) + self.dp(m, n, i, j+1)
        if i < m and j >= n-1:
            return self.dp(m, n, i+1, j)
        if i >= m-1 and j < n:
            return self.dp(m, n, i, j+1)