class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        if obstacleGrid[0][0] == 0:
            dp[0][0] = 1
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    if j-1 >= 0 and i-1 >= 0:
                        dp[i][j] = dp[i-1][j] + dp[i][j-1]
                    elif i-1 >=0 and j-1 < 0:
                        dp[i][j] = dp[i-1][j]
                    elif j-1 >= 0 and i-1 < 0:
                        dp[i][j] = dp[i][j-1]
        return dp[m-1][n-1]