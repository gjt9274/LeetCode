class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 逻辑上将二维矩阵展平成一维，然后进行二分搜索
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        row = len(matrix)
        col = len(matrix[0])
        left, right = 0, row*col - 1
        while left <= right:
            mid = left + (right - left) // 2
            val = matrix[mid//col][mid % col] #求中点的值
            if val == target:
                return True
            elif val < target:
                left = mid + 1
            elif val > target:
                right = mid - 1
        return False
