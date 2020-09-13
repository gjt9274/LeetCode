class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(grid, i, j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]): #判断边界
                return 0
            if grid[i][j] != '1': #判断是否是岛屿
                return 0
            grid[i][j] = '2' #标记为已访问
            return dfs(grid, i-1, j) + dfs(grid, i+1, j) + dfs(grid, i, j+1)+dfs(grid, i, j-1) + 1

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1' and dfs(grid, i, j) >= 1:
                    count += 1
        return count
