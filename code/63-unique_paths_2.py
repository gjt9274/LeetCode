class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        # 定义状态
        d = [[0] * n for _ in range(m)]

        # 初始化
        i = 0
        while i < m and obstacleGrid[i][0] != 1:
            d[i][0] = 1
            i += 1

        j = 0
        while j < n and obstacleGrid[0][j] != 1:
            d[0][j] = 1
            j += 1

        # 状态转移方程
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] != 1:
                    d[i][j] = d[i][j-1] + d[i-1][j]

        return d[m-1][n-1]
