class Solution:
    def findDiagonalOrder(self, matrix):
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return []
        m, n = len(matrix), len(matrix[0])
        s = 0  # s是i+j 的和
        res = []
        while s < m+n:
            x1 = s if s < m else m-1
            y1 = s - x1
            while x1 >= 0 and y1 < n:
                res.append(matrix[x1][y1])
                x1 -= 1
                y1 += 1
            s += 1

            if s >= m+n:
                break

            y2 = s if s < n else n-1
            x2 = s - y2
            while y2 >= 0 and x2 < m:
                res.append(matrix[x2][y2])
                x2 += 1
                y2 -= 1
            s += 1
        return res
