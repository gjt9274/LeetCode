class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # 定义状态
        d = [[0] * n for _ in range(m)]  # 每一项代表从start位置到该位置的路径总数

        # 初始化
        for i in range(m):
            d[i][0] = 1
        for j in range(n):
            d[0][j] = 1

        # 状态转移方程
        for i in range(1, m):
            for j in range(1, n):
                d[i][j] = d[i-1][j] + d[i][j-1]

        return d[m-1][n-1]
