class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        q = []
        cnt = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    q.append((i, j))
                    cnt += 1
                else:
                    grid[i][j] = -1

        if cnt == 0 or cnt == len(grid) * len(grid[0]):
            return -1

        maxDis = 1

        while q:
            x, y = q.pop(0)
            for bias in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                newX = x + bias[0]
                newY = y + bias[1]
                if 0 <= newX < len(grid) and 0 <= newY < len(grid[0]) and grid[newX][newY] == -1:
                    grid[newX][newY] = grid[x][y] + 1
                    q.append((newX, newY))
                    maxDis = max(maxDis, grid[x][y])

        return maxDis
