class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        # 定义状态
        d = [0] * n

        # 初始化
        d[0] = 1
        d[1] = 2

        # 状态转移方程
        for i in range(2, n):
            d[i] = d[i-1] + d[i-2]

        return d[n-1]
