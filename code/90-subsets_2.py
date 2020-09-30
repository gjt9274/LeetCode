class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # 先排序
        res = []

        def backtrack(nums, path, start):
            # 终止条件
            res.append(path)
            # 选择列表
            for i in range(start, len(nums)):
                # 剪枝，去掉当前列表中，与前一个数相同的数产生的分支，所以要先将nums排序
                if i > start and nums[i] == nums[i-1]:
                    continue
                # 做出选择
                path = path + [nums[i]]
                # 递归下一层
                backtrack(nums, path, i+1)
                # 回溯
                path = path[:-1]
        backtrack(nums, [], 0)
        return res
