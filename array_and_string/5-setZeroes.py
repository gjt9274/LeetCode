class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        """
        思路：
        1. 遍历数组，如果 matrix[i][j] == 0，则将该行的首元素和该列的首元素设置为0，作为标志
        即 
           if matrix[i][j] == 0:
               matrix[0][j] = 0
               matrix[i][0] = 0
        2. 再次遍历数组中，根据行首和列首元素标志，将矩阵置零
        3. 如果第一行或者第一列有 0 ，会把 matrix[0][0] 设置为0，这样会把第一行和第一列都清零，需要特殊处理
        """
        firstRowHasZero = False
        firstColHasZero = False
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    if i == 0:
                        firstRowHasZero = True
                    if j == 0:
                        firstColHasZero = True
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        for i in range(1,len(matrix)):
            for j in range(1,len(matrix[0])):
                if matrix[i][0] == 0 || matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        if firstRowHasZero:
            for j in range(len(matrix[0])):
                matrix[0][j] = 0
        if firstColHasZero:
            for i in range(len(matrix)):
                matrix[i][0] = 0

