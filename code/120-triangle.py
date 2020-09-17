#自顶向下
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        d = [[0]*n for _ in range(n)]
        d[0][0] = triangle[0][0]
        for i in range(1,n):
            d[i][0] = d[i-1][0] + triangle[i][0] #注意每一行的开头
            for j in range(1,i):
                d[i][j] = min(d[i-1][j-1],d[i-1][j]) + triangle[i][j]  #状态转移方程
            d[i][i] = d[i-1][i-1] + triangle[i][i] #注意每一行的结尾
        
        return min(d[n-1])

# 自底向上
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        d = [[0]*n for _ in range(n)]
        for i in range(len(triangle[n-1])):
            d[n-1][i] = triangle[n-1][i]

        for i in range(n-2,-1,-1):
            for j in range(len(triangle[i])):
                d[i][j] = min(d[i+1][j],d[i+1][j+1]) + triangle[i][j]
        
        return d[0][0]