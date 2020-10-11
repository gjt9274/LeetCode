class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res, path = [], []

        def backtrack(nums, path, start):
            # 终止条件
            res.append(path)
            # 找选择列表
            for i in range(start, len(nums)):
                # 做出选择
                path = path + [nums[i]] #append是以引用形式添加，会导致res与path一样
                # 递归进入
                backtrack(nums, path, i+1)
                # 回溯
                path = path[:-1]

        backtrack(nums, path, 0)
        return res
