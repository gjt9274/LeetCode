class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @return: The maximum size
    """

    def backPack(self, m, A):
        # write your code here
        # 定义状态
        dp = [0] * (m+1)
        # 初始化
        dp[0] = 0
        # 状态转移
        for i in range(1, m+1):
            for s in A:
                if i-s < 0:
                    continue
                dp[i] = max(dp[i], s + dp[i-s])
        return dp[m]


if __name__ == "__main__":
    m = 10
    A = [3, 4, 8, 5]
    solution = Solution()
    print(solution.backPack(m,A))