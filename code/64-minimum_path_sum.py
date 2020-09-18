class Solution:
    def minPathSum(self, grid) :
        m = len(grid)
        n = len(grid[0])
        if m == 0 or n==0:
            return 0
        # 定义状态
        d = [[0]*n for _ in range(m)]

        # 初始化
        d[0][0] = grid[0][0]
        tmp = 0
        for i in range(1,m):
            d[i][0] = d[i-1][0] + grid[i][0]
        
        tmp = 0
        for i in range(1,n):
            d[0][i] = d[0][i-1] + grid[0][i]

        # 状态转移方程
        for i in range(1,m):
            for j in range(1,n):
                d[i][j] = min(d[i-1][j],d[i][j-1]) + grid[i][j]
        
        return d[m-1][n-1]

if __name__ == "__main__":
    s = Solution()
    grid = [
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]
    ]
    d= s.minPathSum(grid)
