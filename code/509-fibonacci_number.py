class Solution:
    #普通递归
    def fib(self, N: int) -> int:
        if N < 2:
            return N

        return self.fib(N-1) + self.fib(N-2)


class Solution:
    def fib(self, N: int) -> int:

        m = [0] * (N+1)
        #带备忘录的递归

        def helper(n):
            nonlocal m
            if n < 2:
                return n
            if m[n] != 0:
                return m[n]

            ans = helper(n-1) + helper(n-2)
            m[n] = ans
            return ans

        return helper(N)


#动态规划
class Solution:
    def fib(self, N: int) -> int:
        if N < 2:
            return N
        # 状态
        dp = [0] * (N+1)

        # 初始化
        dp[1] = 1

        # 状态转移方程
        for i in range(2, N+1):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[N]
