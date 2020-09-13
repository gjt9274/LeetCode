class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        def area(grid, i, j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):  # 判断边界
                return 0

            if grid[i][j] != 1:  # 判断是否是岛屿
                return 0

            grid[i][j] = 2  # 标记已被访问

            return area(grid, i-1, j)+area(grid, i+1, j)+area(grid, i, j-1)+area(grid, i, j+1) + 1

        maxArea = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    a = area(grid, i, j)
                    maxArea = max(a, maxArea)
        return maxArea
