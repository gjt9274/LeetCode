class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:

        q = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    q.append((i, j))
                else:
                    matrix[i][j] = -1

        while q:
            x, y = q.pop(0)
            for x_bias, y_bias in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                new_x = x + x_bias
                new_y = y + y_bias
                if 0 <= new_x < len(matrix) and 0 <= new_y < len(matrix[0]) and matrix[new_x][new_y] == -1:
                    matrix[new_x][new_y] = matrix[x][y] + 1
                    q.append([new_x, new_y])  # 将新扩展的点加入队列
        return matrix
